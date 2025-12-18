from PiPERControllerMK2 import PiPERControllerMK2
from Picus2Controller import Picus2Controller
from piper_sdk import *
from PyArduino import PyArduino
import time

class LOHCActionBook():
    def __init__(self):
        """
        This function initialize two auxillary modules and PiPER CAN modules. And also check if it's valid

        Input : None
        Output : None
        """
        self.pa = PyArduino()
        self.p2c = Picus2Controller("/dev/ttyACM1")

        self.piper_arm_right = PiPERControllerMK2(C_PiperInterface("piper_right"))
        self.piper_arm_left = PiPERControllerMK2(C_PiperInterface("piper_left"))

        self.railmagnet = 2

        print("init")

        self.speed_slow = 15
        self.speed_default = 70
        self.speed_fast = 90

        self.piper_arm_right.run_move_joint([0, 0, 0, 0, 0, 0, 0])
        self.piper_arm_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])

        self.pa.run_digital_write(self.railmagnet, True)

    # def run_lohc_action_1(self):
    #     """
    #     This function contains motion for action 1 : Pouring powder to bowl

    #     Input : None
    #     Output : None
    #     """
    #     gripper_close = 40

    #     print("Action1")PiPERController/mk2/LOHCActionAll.py

    #     # 1 Initialization Position 
    #     self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], self.speed_default)
    #     self.piper_arm_right.run_piper_movement([87, -3, -41, 2, 50, -3, 76, -4, -43, 347, -134, 87, -46, 76], self.speed_default)

    #     # 2 Close bottle and grap it
    #     origin_position = [79, 4, -25, 17, 26, -22, 76, -7, 29, 310, -85, 84, 2, 76]
    #     self.piper_arm_right.run_piper_movement([79, 4, -25, 17, 26, -22, 76, -7, 29, 310, -85, 84, 2, 76], self.speed_default)

    #     self.piper_arm_right.run_piper_movement([91, 18, -24, -2, 14, 0, 76, 0, 77, 310, -141, 86, -51, 76], self.speed_slow)
    #     self.piper_arm_right.run_piper_movement([91, 18, -24, -2, 14, 0, gripper_close, 0, 77, 310, -141, 86, -51, gripper_close], self.speed_slow)
    #     self.piper_arm_right.run_move_linear_known([0, 77, 310 + 100, -141, 86, -51, gripper_close], self.speed_slow)

    #     # Move to Macja
    #     self.piper_arm_right.run_piper_movement([26, 29, -47, 2, 21, 4, gripper_close, 78, 39, 414, 73, 84, 100, gripper_close], self.speed_default)
    #     self.piper_arm_right.run_piper_movement([-30, 40, -38, -4, 2, -1, gripper_close, 128, -73, 371, -77, 86, -107, -2], self.speed_default)
    #     self.piper_arm_right.run_piper_movement([-20, 49, -22, -3, -36, 1, gripper_close, 163, -58, 309, -8, 76, -27, -3], self.speed_default)

    #     # Pour it with little pounding for 2 times
    #     self.piper_arm_right.run_piper_movement([-28, 53, -6, -16, -42, 11, gripper_close, 142, -57, 222 + 75, -93, 89, -110, gripper_close], self.speed_default)
    #     self.piper_arm_right.run_piper_movement([-14, 52, -18, 13, -11, 118, gripper_close, 167, -45, 242 + 75, 112, -37, 60, gripper_close], self.speed_slow, time_out = 5)
    #     time.sleep(2)
    #     self.piper_arm_right.run_piper_movement([-14, 57, -23, 67, -13, 122, gripper_close, 180, -64, 244 + 75, -172, -67, -35, gripper_close], self.speed_slow, time_out = 5)
    #     time.sleep(2)
    #     self.piper_arm_right.run_piper_movement([-14, 52, -18, 13, -11, 118, gripper_close, 167, -45, 242 + 75, 112, -37, 60, gripper_close], self.speed_slow, time_out = 5)
    #     time.sleep(2)

    #     self.piper_arm_right.run_move_joint([-28, 53, -30, -16, -42, 11, gripper_close])

    #     self.piper_arm_right.run_piper_movement([-28, 53, -6, -16, -42, 11, gripper_close, 142, -57, 222 + 75, -93, 89, -110, gripper_close], self.speed_default)
    #     self.piper_arm_right.run_piper_movement([-14, 52, -18, 13, -11, 118, gripper_close, 167, -45, 242 + 75, 112, -37, 60, gripper_close], self.speed_slow, time_out = 5)
    #     time.sleep(2)
    #     self.piper_arm_right.run_piper_movement([-14, 57, -23, 67, -13, 122, gripper_close, 180, -64, 244 + 75, -172, -67, -35, gripper_close], self.speed_slow, time_out = 5)
    #     time.sleep(2)
    #     self.piper_arm_right.run_piper_movement([-14, 52, -18, 13, -11, 118, gripper_close, 167, -45, 242 + 75, 112, -37, 60, gripper_close], self.speed_slow, time_out = 5)
    #     time.sleep(2)

    #     self.piper_arm_right.run_move_joint([-28, 53, -30, -16, -42, 11, gripper_close])

    #     # Move to stand
    #     self.piper_arm_right.run_piper_movement([-20, 49, -22, -3, -36, 1, gripper_close, 163, -58, 309, -8, 76, -27, -3], self.speed_default)
    #     self.piper_arm_right.run_piper_movement([-30, 40, -38, -4, 2, -1, gripper_close, 128, -73, 371, -77, 86, -107, -2], self.speed_default)
    #     self.piper_arm_right.run_piper_movement([26, 29, -47, 2, 21, 4, gripper_close, 78, 39, 414, 73, 84, 100, gripper_close], self.speed_default)
    #     self.piper_arm_right.run_move_linear_known([0, 77, 310 + 100, -141, 86, -51, gripper_close], self.speed_default, time_out = 15)

    #     # Release bottle and return
    #     self.piper_arm_right.run_move_linear_known([0, 77, 310, -141, 86, -51, gripper_close], self.speed_default, time_out = 15)
    #     self.piper_arm_right.run_piper_movement([91, 18, -24, -2, 14, 0, 76, 0, 77, 310, -141, 86, -51, 76], self.speed_slow)
    #     self.piper_arm_right.run_piper_movement([79, 4, -25, 17, 26, -22, 76, -7, 29, 310, -85, 84, 2, 76], self.speed_default)

    #     self.piper_arm_right.run_piper_movement([87, -3, -41, 2, 50, -3, 76, -4, -43, 347, -134, 87, -46, 76], self.speed_default)
    #     self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], self.speed_default)
            
    
    # def run_test(self):
    #     """
    #     This function contains test curve motions.

    #     Input : None
    #     Output : None
    #     """
    #     self.piper_arm_left.run_move_curve([
    #         [60, 0, 250, 0, 85, 0, 0x01], # 출발점
    #         [200, 0, 400, 0, 85, 0, 0x02], # 경유점
    #         [60, 0, 550, 0, 85, 0, 0x03], # 도착점
    #         ])
    #     time.sleep(15)
    #     self.piper_arm_left.run_move_curve([
    #         [60, 0, 550, 0, 85, 0, 0x01], # 출발점
    #         [200, 0, 400, 0, 85, 0, 0x02], # 경유점
    #         [60, 0, 250, 0, 85, 0, 0x03], # 도착점
    #         ])
    #     time.sleep(15)

    def run_lohc_action_3(self):
        """
        This function contains motion for action 3 : using pippette on bowl
        #WIP#

        Input : None
        Output : None
        """
        print("Action 3")

        gripper_close = 0
        movement_y = 70
        movement_z = 170
        distance = 15
        wait = 3

        # 1. Set Pose
        self.piper_arm_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])
        self.piper_arm_left.run_piper_movement([0, 20, -32, -1, 19, -3, 0, 74, 1, 347, -108, 86, -107, 74], self.speed_default)

        self.piper_arm_left.run_move_joint([90, 20, -32, -1, 19, -3, 0, 74])
        self.piper_arm_left.run_move_joint([140, 20, -32, -1, 19, -3, 0, 74])
        self.piper_arm_left.run_move_joint([140, 20, -32, 93, 19, -3, 0, 74])
        self.piper_arm_left.run_move_joint([140, 20, -32, 93, 19, -3, 0, 74])
        self.piper_arm_left.run_piper_movement([133, 96, -39, 50, -66, -25, 71, -158, 266, 221, 53, 86, 140, 74], self.speed_default)

        # 2. Approach target

        self.piper_arm_left.run_piper_movement([133, 96, -39, 50, -66, -25, 71, -158, 266, 221, 53, 86, 140, 74], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([-158, 269 + movement_y, 221, -91, 90, 0, 74], self.speed_default)
        self.piper_arm_left.run_move_linear_known([-158, 269 + movement_y, 221, -91, 90, 0, 74])

         # 3. Escpae
        
        self.piper_arm_left.run_move_linear_known([-158, 333, 221 + movement_z, -91, 90, 0, gripper_close], self.speed_default)
        self.piper_arm_left.run_move_linear_known([-158, 333, 221 + movement_z, -91, 90, 0, gripper_close])

        self.piper_arm_left.run_move_linear_known([-158, 333 - movement_y, 395, -91, 90, 0, gripper_close], self.speed_default)
        self.piper_arm_left.run_move_linear_known([-158, 333 - movement_y, 395, -91, 90, 0, gripper_close])
        self.piper_arm_left.run_move_linear_known([-158, 150, 395, -91, 90, 0, gripper_close], self.speed_default)
        self.piper_arm_left.run_move_linear_known([81, 110, 395, 65, 89, 119, gripper_close], self.speed_default)

        # # 4. Pippeting 
        self.piper_arm_left.run_piper_movement([18, 42, -43, 1, 0, 1, gripper_close, 147, 47, 399, 19, 83, 37, gripper_close], self.speed_default)
        self.piper_arm_left.run_piper_movement([19, 42, -24, -2, -11, 4, gripper_close, 148, 53, 303, 138, 87, 158, gripper_close]) # 5 

        self.piper_arm_left.run_move_linear_known([148 + distance, 53 + distance, 303, 138, 87, 158, gripper_close], self.speed_slow) # 1
        time.sleep(wait)
        # self.piper_arm_left.run_move_linear_known([148, 53 + distance, 303, 138, 87, 158, gripper_close], self.speed_slow) # 2
        # time.sleep(wait) 
        # self.piper_arm_left.run_move_linear_known([148 - distance, 53 + distance, 303, 138, 87, 158, gripper_close], self.speed_slow) # 3
        # time.sleep(wait)
        # self.piper_arm_left.run_move_linear_known([148 - distance, 53, 303, 138, 87, 158, gripper_close], self.speed_slow) # 6
        # time.sleep(wait)
        # self.piper_arm_left.run_move_linear_known([148 - distance, 53 - distance, 303, 138, 87, 158, gripper_close], self.speed_slow) # 9 
        # time.sleep(wait)
        # self.piper_arm_left.run_move_linear_known([148, 53 - distance, 303, 138, 87, 158, gripper_close], self.speed_slow) # 8
        # time.sleep(wait)
        # self.piper_arm_left.run_move_linear_known([148 + distance, 53 - distance, 303, 138, 87, 158, gripper_close], self.speed_slow) # 7
        # time.sleep(wait)
        # self.piper_arm_left.run_move_linear_known([148 + distance, 53, 303, 138, 87, 158, gripper_close], self.speed_slow) # 4
        # time.sleep(wait)
        self.piper_arm_left.run_move_linear_known([148, 53, 303, 138, 87, 158, gripper_close], self.speed_slow) # 5
        time.sleep(wait)

        # # inverse replay
        self.piper_arm_left.run_piper_movement([18, 42, -43, 1, 0, 1, gripper_close, 147, 47, 399, 19, 83, 37, gripper_close], self.speed_fast)

        # self.piper_arm_left.run_move_linear_known([81, 110, 395, 65, 89, 119, gripper_close], self.speed_fast)
        self.piper_arm_left.run_piper_movement([107, 39, -44, 100, -46, -104, gripper_close, 28, 125, 396, -62, 90, 0, gripper_close])
        self.piper_arm_left.run_piper_movement([150, 68, -57, 86, -59, -83, gripper_close, -158, 181, 395, -91, 90, 0, gripper_close])
        self.piper_arm_left.run_move_linear_known([-158, 181 + movement_y, 395, -91, 90, 0, gripper_close], self.speed_default)
        self.piper_arm_left.run_move_linear_known([-158, 181 + movement_y, 395, -91, 90, 0, gripper_close])
        self.piper_arm_left.run_move_linear_known([-158, 337, 395, -91, 90, 0, gripper_close]) #y=335

        self.piper_arm_left.run_move_linear_known([-158, 330, 395 - movement_z, -91, 90, 0, gripper_close], self.speed_default)
        self.piper_arm_left.run_move_linear_known([-158, 330, 395 - movement_z, -91, 90, 0, gripper_close])
        self.piper_arm_left.run_move_linear_known([-158, 330, 221, -91, 90, 0, 74]) #330

        
        self.piper_arm_left.run_move_linear_known([-158, 332 - movement_y, 221, -91, 90, 0, 74], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([-158, 332 - movement_y, 221, -91, 90, 0, 74])
        self.piper_arm_left.run_move_linear_known([-158, 256, 221, -91, 90, 0, 74], self.speed_slow)
        self.piper_arm_left.run_piper_movement([133, 96, -39, 50, -66, -25, 71, -158, 266, 221, 53, 86, 140, 74], self.speed_slow)

        self.piper_arm_left.run_piper_movement([133, 96, -39, 50, -66, -25, 71, -158, 266, 221, 53, 86, 140, 74], self.speed_default)
        self.piper_arm_left.run_move_joint([140, 20, -32, 93, 19, -3, 0, 74], self.speed_default)
        self.piper_arm_left.run_move_joint([140, 20, -32, 93, 19, -3, 0, 74])
        self.piper_arm_left.run_move_joint([140, 20, -32, -1, 19, -3, 0, 74])
        self.piper_arm_left.run_move_joint([90, 20, -32, -1, 19, -3, 0, 74])
        
        self.piper_arm_left.run_piper_movement([0, 20, -32, -1, 19, -3, 0, 74, 1, 347, -108, 86, -107, 74], self.speed_default)
        self.piper_arm_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])

        
        
        
        
        

if __name__ == "__main__":
    lab = LOHCActionBook()
    for i in range(3):
        # lab.run_lohc_action_1() #shinyoung
        # lab.run_rail_to_left() #me - 7
        # lab.run_lohc_action_4() #me
        # lab.run_lohc_action_6() #me
        lab.run_lohc_action_3() #shinyoung
        # lab.run_rail_to_right() #me - 7
        # lab.run_lohc_action_8_2() #me
        # lab.run_test()