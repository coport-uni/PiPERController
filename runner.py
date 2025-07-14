from typing import (
    Optional,
)
from piper_sdk import *
import time
import os
import csv
from waiting import *
from tqdm import tqdm

class PiperController():
    def __init__(self):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        self.time_delay = 0.005
        self.downsampling_rate = 50
        self.motion_factor = 1000

        # Initialize connection
        os.system("bash find_all_can_port.sh")
        os.system("bash can_activate.sh piper_left 1000000 \"3-1:1.0\"")
        time.sleep(1)
        self.piper_left = C_PiperInterface_V2("piper_left")
        self.piper_left.ConnectPort()
        self.piper_left.ArmParamEnquiryAndConfig(0x01,0x02,0,0,0x02)
        
        # Reset PiPER
        # self.piper_left.MotionCtrl_1(0x02,0,0)
        # self.piper_left.MotionCtrl_2(0, 0, 0, 0x00)

        # Enable PiPER
        while not self.piper_left.EnablePiper():
            time.sleep(0.01)
        
    def get_position_gripper(self):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        message = str(self.piper_left.GetArmGripperMsgs())

        gripper_index_string = ["grippers_angle: ", ","]

        gripper_index_number = [0,0]

        for index_number in range(2):
            gripper_index_number[index_number] = message.find(gripper_index_string[index_number])

        gripper_state = round(int(message[gripper_index_number[0] + 16:gripper_index_number[1]]) / self.motion_factor)

        return gripper_state

    def get_position_joint(self):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        message = str(self.piper_left.GetArmJointMsgs())

        joint_index = [0, 0, 0, 0, 0, 0, 0]
        joint_state = [0, 0, 0, 0, 0, 0, 0]
        
        for index_number in range(6):
            joint_index[index_number] = message.find(f"Joint {index_number + 1}:")

        for joint_number in range(6):
            joint_state[joint_number] = round(int(message[joint_index[joint_number] + 8:joint_index[joint_number + 1] - 1]) / self.motion_factor)

        joint_state[6] = self.get_position_gripper()

        return joint_state

    def get_position_eef(self): 
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        message = str(self.piper_left.GetArmEndPoseMsgs())
        eef_index_string = ["X_axis : ", "Y_axis : ", "Z_axis : ", "RX_axis : ", "RY_axis : ", "RZ_axis : "]

        eef_index = [0, 0, 0, 0, 0, 0, 0]
        eef_state = [0, 0, 0, 0, 0, 0, 0]

        for index_number in range(6):
            eef_index[index_number] = message.find(eef_index_string[index_number])
        
        for eef_number in range(6):
            eef_state[eef_number] = round(int(message[eef_index[eef_number] + 9:eef_index[eef_number + 1] - 1]) / self.motion_factor)

        eef_state[6] = self.get_position_gripper()

        return eef_state

    def get_normalized_value(self, value_max : int, value_min : int, value_input : int):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        # if value_min <= value_input <= value_max:

        #     return value_input * self.motion_factor
        
        # elif value_min > value_input:

        #     return value_input * self.motion_factor
        
        # elif value_input > value_max:

        #     return value_input * self.motion_factor

        return value_input * self.motion_factor
    
    def get_arm_status(self):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        message = str(self.piper_left.GetArmStatus())

        armstatus_index_string = ["Motion Status: ", "Trajectory Num: "]
        armstatus_success_string = "REACH_TARGET_POS_SUCCESSFULLY(0x0)"

        armstatus_index_number = [0,0]

        for index_number in range(2):
            armstatus_index_number[index_number] = message.find(armstatus_index_string[index_number])

        armstatus_state = message[armstatus_index_number[0] + 15:armstatus_index_number[1] - 1]

        if armstatus_state == armstatus_success_string:

            time.sleep(self.time_delay)
            return True

        else: 
            
            return False

    def get_record_csv(self, filepath : str, value_input : list):
        with open(filepath, mode = 'a', newline = '') as csvfile:
            value_writer = csv.writer(csvfile, lineterminator = '\n')
            value_writer.writerow([value_input])
            csvfile.close()
        time.sleep(self.time_delay * self.downsampling_rate)

    def run_position_gripper(self, gripper_mm : int):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        self.piper_left.GripperCtrl(0,1000,0x02, 0)
        gripper_mm = self.get_normalized_value(70, -5, gripper_mm)
        self.piper_left.GripperCtrl(gripper_mm, 5000, 0x01, 0)

        return True
    
    def run_position_joint(self, joint_value_input : list):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        self.piper_left.MotionCtrl_2(0x01, 0x01, 100, 0x00)

        joint_value_input[0] = self.get_normalized_value(145, -145, joint_value_input[0])
        joint_value_input[1] = self.get_normalized_value(175, 5, joint_value_input[1])
        joint_value_input[2] = self.get_normalized_value(160, 0, joint_value_input[2])
        joint_value_input[3] = self.get_normalized_value(95, -95, joint_value_input[3])
        joint_value_input[4] = self.get_normalized_value(70, -70, joint_value_input[4])
        joint_value_input[5] = self.get_normalized_value(115, -115, joint_value_input[5])

        self.piper_left.JointCtrl(joint_value_input[0], joint_value_input[1], joint_value_input[2], joint_value_input[3], joint_value_input[4], joint_value_input[5])
        self.run_position_gripper(joint_value_input[6])
        
        time.sleep(self.time_delay * self.downsampling_rate)

        # wait(lambda: self.get_arm_status(), timeout_seconds = 2, waiting_for="Finish of movement")

        return True
    
    def run_position_eef(self, eef_value_input : list):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        self.piper_left.MotionCtrl_2(0x01, 0x00, 100, 0x00)

        current_eef_value = self.get_position_eef()

        for index_number in range(6):
            eef_value_input[index_number] = int(((current_eef_value[index_number] + eef_value_input[index_number])) * self.motion_factor)


        self.piper_left.EndPoseCtrl(eef_value_input[0], eef_value_input[1], eef_value_input[2], eef_value_input[3], eef_value_input[4], eef_value_input[5])
        self.run_position_gripper(eef_value_input[6])
        
        # wait(lambda: self.get_arm_status(), timeout_seconds = 2, waiting_for="Finish of movement")
        
        return True

    def run_initialization(self):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        self.piper_left.GripperCtrl(0,1000,0x01, 0xAE)
        time.sleep(self.time_delay)
        self.piper_left.GripperCtrl(0,1000,0x00, 0)

        self.run_position_joint([0, 0, 0, 0, 0, 0, 0])
        wait(lambda: self.get_arm_status(), timeout_seconds = 2, waiting_for="Finish of movement")

        return True

    def run_record_csv(self, filepath : str):

        restored_value = [0, 0, 0, 0, 0, 0, 0]
        row_count = 0

        with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
            value_reader = csv.reader(csvfile, lineterminator = '\n')
            for row_data in value_reader:
                processed_data = str(row_data).replace("'", "").replace("[", "").replace("]", "").split(",")
                # print(processed_data)
                for index_number in range(7):
                    restored_value[index_number] = int(processed_data[index_number])
                
                # print(restored_value)
                self.run_position_joint(restored_value)
                row_count = row_count + 1
                print(row_count)
                
def main():
    '''
    This function captures live mouse position.

    Input : None
    Output : dict
    '''
    pc = PiperController()
    csv_filepath_down = "action_csv/test_demo_down.csv"
    csv_filepath_up = "action_csv/test_demo_up.csv"

    # os.system("source piper/bin/activate")
    # os.system("python3 piper_ctrl_reset.py")
    # time.sleep(1)
    for i in tqdm(range(10), desc="Moving object as designated"):
        pc.run_initialization()
        pc.run_record_csv(csv_filepath_up)
        pc.run_initialization()
        pc.run_record_csv(csv_filepath_down)

    # while True:
    #     data = pc.get_position_joint()
    #     pc.get_record_csv(csv_filepath, data)
    #     print(data)

    # while True:
    #     pc.run_position_joint([-1 + 30, 1, 2, -3, 6, 0, 67])
    #     pc.get_record_csv("test.csv", pc.get_position_joint())
    #     pc.run_position_joint([-1 - 30, 1, 2, -3, 6, 0, 0])
    #     pc.get_record_csv("test.csv", pc.get_position_joint())

    # while True:
    #     pc.run_position_joint([-1 + 30, 1, 2, -3, 6, 0, 67])
    #     pc.run_position_joint([-1 - 30, 1, 2, -3, 6, 0, 0])
    
    # while True:
    #     print(pc.get_position_eef())

    # while True:
    #     print(pc.get_position_joint())
    
if __name__ == "__main__":
    main()