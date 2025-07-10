from typing import (
    Optional,
)
from piper_sdk import *
import time
import os
import csv

class PiperController():
    def __init__(self):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''

        # os.system("bash find_all_can_port.sh")
        # os.system("bash can_activate.sh piper_left 1000000 "3-1:1.0"")
        self.piper_left = C_PiperInterface_V2("piper_left")
        self.piper_left.ConnectPort()
        self.piper_left.ArmParamEnquiryAndConfig(0x01,0x02,0,0,0x02)

        while not self.piper_left.EnablePiper():
            time.sleep(0.01)

        self.time_delay = 1
        self.motion_factor = 1000
    
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
        time.sleep(self.time_delay)

        joint_index = [0, 0, 0, 0, 0, 0, 0]
        joint_state = [0, 0, 0, 0, 0, 0, 0]
        
        for index_number in range(6):
            joint_index[index_number] = message.find(f"Joint {index_number + 1}:")

        for joint_number in range(6):
            joint_state[joint_number] = int(int(message[joint_index[joint_number] + 8:joint_index[joint_number + 1] - 1]) / self.motion_factor)

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
            eef_state[eef_number] = int(int(message[eef_index[eef_number] + 9:eef_index[eef_number + 1] - 1]) / self.motion_factor)

        eef_state[6] = self.get_position_gripper()

        return eef_state

    def get_normalized_value(self, value_max : int, value_min : int, value_input : int):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        if value_min <= value_input <= value_max:

            return value_input * self.motion_factor
        
        elif value_min > value_input:

            return value_min * self.motion_factor
        
        elif value_input > value_max:

            return value_max * self.motion_factor

    def run_position_gripper(self, gripper_mm : int):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        gripper_mm = self.get_normalized_value(68, -2, gripper_mm)
        self.piper_left.GripperCtrl(0,1000,0x02, 0)
        # print(gripper_mm)
        self.piper_left.GripperCtrl(gripper_mm, 1000, 0x01, 0)
        time.sleep(0.005)

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

        print(eef_value_input)
        self.piper_left.EndPoseCtrl(eef_value_input[0], eef_value_input[1], eef_value_input[2], eef_value_input[3], eef_value_input[4], eef_value_input[5])
        self.run_position_gripper(eef_value_input[6])
        
        return True
        
    def get_record_csv(self, value_input):
        with open('test.csv', mode = 'a', newline = '') as csvfile:
            spamwriter = csv.writer(csvfile, lineterminator = '\n')
            spamwriter.writerow([value_input])
            csvfile.close()

def main():
    '''
    This function captures live mouse position.

    Input : None
    Output : dict
    '''
    pc = PiperController()
    delay_time = 2

    pc.run_position_joint([0, 0, 0, 0, 0, 0, 0])
    time.sleep(delay_time)

    # while True:
    #     pc.run_position_eef([0, 0, 30, 0, 0, 0, 67])
    #     time.sleep(delay_time)
    #     pc.run_position_eef([0, 0, -30, 0, 0, 0, 0])
    #     time.sleep(delay_time)

    while True:
        pc.run_position_joint([-1 + 30, 1, 2, -3, 6, 0, 67])
        time.sleep(delay_time)
        pc.run_position_joint([-1 - 30, 1, 2, -3, 6, 0, 0])
        time.sleep(delay_time)

    # while True:
    #     print(pc.get_position_eef())

    # while True:
    #     print(pc.get_position_joint())
    
if __name__ == "__main__":
    main()