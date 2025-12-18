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

        self.speed_slow = 10
        self.speed_default = 20
        self.speed_fast = 90

        self.piper_arm_right.run_move_joint([0, 0, 0, 0, 0, 0, 0])
        self.piper_arm_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])

        self.pa.run_digital_write(self.railmagnet, True)

    def run_lohc_action_1(self):
        """
        This function contains motion for action 1 : Pouring powder to bowl

        Input : None
        Output : None
        """
        gripper_close = 40

        print("Action1")

        # 1 Initialization Position 
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], self.speed_default)
        self.piper_arm_right.run_piper_movement([87, -3, -41, 2, 50, -3, 76, -4, -43, 347, -134, 87, -46, 76], self.speed_default)

        # 2 Close bottle and grap it
        origin_position = [79, 4, -25, 17, 26, -22, 76, -7, 29, 310, -85, 84, 2, 76]
        self.piper_arm_right.run_piper_movement([79, 4, -25, 17, 26, -22, 76, -7, 29, 310, -85, 84, 2, 76], self.speed_default)

        self.piper_arm_right.run_piper_movement([91, 18, -24, -2, 14, 0, 76, 0, 77, 310, -141, 86, -51, 76], self.speed_slow)
        self.piper_arm_right.run_piper_movement([91, 18, -24, -2, 14, 0, gripper_close, 0, 77, 310, -141, 86, -51, gripper_close], self.speed_slow)
        self.piper_arm_right.run_move_linear_known([0, 77, 310 + 100, -141, 86, -51, gripper_close], self.speed_slow)

        # Move to Macja
        self.piper_arm_right.run_piper_movement([26, 29, -47, 2, 21, 4, gripper_close, 78, 39, 414, 73, 84, 100, gripper_close], self.speed_default)
        self.piper_arm_right.run_piper_movement([-30, 40, -38, -4, 2, -1, gripper_close, 128, -73, 371, -77, 86, -107, -2], self.speed_default)
        self.piper_arm_right.run_piper_movement([-20, 49, -22, -3, -36, 1, gripper_close, 163, -58, 309, -8, 76, -27, -3], self.speed_default)

        # Pour it with little pounding for 2 times
        self.piper_arm_right.run_piper_movement([-28, 53, -6, -16, -42, 11, gripper_close, 142, -57, 222 + 75, -93, 89, -110, gripper_close], self.speed_default)
        self.piper_arm_right.run_piper_movement([-14, 52, -18, 13, -11, 118, gripper_close, 167, -45, 242 + 75, 112, -37, 60, gripper_close], self.speed_slow, time_out = 5)
        time.sleep(2)
        self.piper_arm_right.run_piper_movement([-14, 57, -23, 67, -13, 122, gripper_close, 180, -64, 244 + 75, -172, -67, -35, gripper_close], self.speed_slow, time_out = 5)
        time.sleep(2)
        self.piper_arm_right.run_piper_movement([-14, 52, -18, 13, -11, 118, gripper_close, 167, -45, 242 + 75, 112, -37, 60, gripper_close], self.speed_slow, time_out = 5)
        time.sleep(2)

        self.piper_arm_right.run_move_joint([-28, 53, -30, -16, -42, 11, gripper_close])

        self.piper_arm_right.run_piper_movement([-28, 53, -6, -16, -42, 11, gripper_close, 142, -57, 222 + 75, -93, 89, -110, gripper_close], self.speed_default)
        self.piper_arm_right.run_piper_movement([-14, 52, -18, 13, -11, 118, gripper_close, 167, -45, 242 + 75, 112, -37, 60, gripper_close], self.speed_slow, time_out = 5)
        time.sleep(2)
        self.piper_arm_right.run_piper_movement([-14, 57, -23, 67, -13, 122, gripper_close, 180, -64, 244 + 75, -172, -67, -35, gripper_close], self.speed_slow, time_out = 5)
        time.sleep(2)
        self.piper_arm_right.run_piper_movement([-14, 52, -18, 13, -11, 118, gripper_close, 167, -45, 242 + 75, 112, -37, 60, gripper_close], self.speed_slow, time_out = 5)
        time.sleep(2)

        self.piper_arm_right.run_move_joint([-28, 53, -30, -16, -42, 11, gripper_close])

        # Move to stand
        self.piper_arm_right.run_piper_movement([-20, 49, -22, -3, -36, 1, gripper_close, 163, -58, 309, -8, 76, -27, -3], self.speed_default)
        self.piper_arm_right.run_piper_movement([-30, 40, -38, -4, 2, -1, gripper_close, 128, -73, 371, -77, 86, -107, -2], self.speed_default)
        self.piper_arm_right.run_piper_movement([26, 29, -47, 2, 21, 4, gripper_close, 78, 39, 414, 73, 84, 100, gripper_close], self.speed_default)
        self.piper_arm_right.run_move_linear_known([0, 77, 310 + 100, -141, 86, -51, gripper_close], self.speed_default, time_out = 15)

        # Release bottle and return
        self.piper_arm_right.run_move_linear_known([0, 77, 310, -141, 86, -51, gripper_close], self.speed_default, time_out = 15)
        self.piper_arm_right.run_piper_movement([91, 18, -24, -2, 14, 0, 76, 0, 77, 310, -141, 86, -51, 76], self.speed_slow)
        self.piper_arm_right.run_piper_movement([79, 4, -25, 17, 26, -22, 76, -7, 29, 310, -85, 84, 2, 76], self.speed_default)

        self.piper_arm_right.run_piper_movement([87, -3, -41, 2, 50, -3, 76, -4, -43, 347, -134, 87, -46, 76], self.speed_default)
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], self.speed_default)
            
    def run_lohc_action_8_1(self):
        """
        This function contains motion for action 8 : Shaking funnel

        Input : None
        Output : None
        """
        movement_z = 75
        gripper_close = 0

        print("Action 8")
        self.piper_arm_right.run_move_joint([0, 0, 0, 0, 0, 0, 0])

        # 1 Initialization Position 
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], self.speed_default)
        self.piper_arm_right.run_piper_movement([-27, 31, -58, -11, 74, 3, 0, 31, -35, 393, -169, 48, 153, 0], self.speed_default)

        # 2 Grap bowl carrier
        self.pa.run_digital_write(self.railmagnet, False)
        self.piper_arm_right.run_piper_movement([-35, 69, -44, 1, 63, -33, 73, 156, -106, 245, -177, 7, 178, 73], self.speed_default)
        self.piper_arm_right.run_move_linear_known([156, -106, 245 - movement_z, -177, 7, 178, 73],self.speed_slow)
        self.piper_arm_right.run_move_linear_known([156, -106, 245 - movement_z, -177, 7, 178, gripper_close],self.speed_slow)

        self.piper_arm_right.run_move_linear_known([156, -106, 245 + movement_z, -177, 7, 178, gripper_close],self.speed_slow)

        # 3 pour bowl carrier
        self.piper_arm_right.run_piper_movement([3, 66, -71, -24, 70, -29, gripper_close, 209, -24, 391, -143, 13, -141, gripper_close], self.speed_slow)
        self.piper_arm_right.run_piper_movement([31, 48, -62, -39, 66, -15, gripper_close, 137, 21, 450, -126, 25, -119, gripper_close], self.speed_slow)
        self.piper_arm_right.run_move_linear_known([130, 91, 400, -89, 1, -89, gripper_close],self.speed_slow)
        time.sleep(5)

        self.piper_arm_right.run_piper_movement([3, 66, -71, -24, 70, -29, gripper_close, 209, -24, 391, -143, 13, -141, gripper_close], self.speed_slow)
        self.piper_arm_right.run_piper_movement([31, 48, -62, -39, 66, -15, gripper_close, 137, 21, 450, -126, 25, -119, gripper_close], self.speed_slow)
        self.piper_arm_right.run_move_linear_known([130, 91, 400, -89, 1, -89, gripper_close],self.speed_slow)
        time.sleep(5)

        self.piper_arm_right.run_piper_movement([3, 66, -71, -24, 70, -29, gripper_close, 209, -24, 391, -143, 13, -141, gripper_close], self.speed_slow)
        
        # 4 return bowl carrier
        self.pa.run_digital_write(self.railmagnet, True)
        self.piper_arm_right.run_piper_movement([-35, 69, -44, 1, 63, -33, gripper_close, 156, -106, 245, -177, 7, 178, gripper_close], self.speed_default)
        self.piper_arm_right.run_move_linear_known([156, -106, 245 - movement_z, -177, 7, 178, gripper_close],self.speed_slow)
        self.piper_arm_right.run_move_linear_known([156, -106, 245 - movement_z -5, -177, 7, 178, 73],self.speed_slow)
        self.piper_arm_right.run_move_linear_known([156, -106, 245, -177, 7, 178, 73],self.speed_slow)

        # 5 Release bowl carrier and return home
        self.piper_arm_right.run_piper_movement([-27, 31, -58, -11, 74, 3, 0, 31, -35, 393, -169, 48, 153, 73], self.speed_default)
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 73], self.speed_default)
    
    def run_lohc_action_8_2(self):
        """
        This function contains motion for action 8 : Pouring bowl to funnel

        Input : None
        Output : None
        """
        movement_z = 100
        gripper_close = 0

        print("Action 8")
        self.piper_arm_right.run_move_joint([0, 0, 0, 0, 0, 0, 0])

        # 1 Initialization Position 
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], self.speed_default)
        self.piper_arm_right.run_piper_movement([33, -2, -28, 1, 38, -1, -2, -2, 0, 310, -171, 88, -137, -2], self.speed_default)
        self.piper_arm_right.run_piper_movement([37, 5, -11, 1, 10, 0, 72, 43, 34, 256, 52, 88, 90, 74], self.speed_slow)

        # 2 Grap funnel carrier
        self.piper_arm_right.run_piper_movement([37, 30, -10, -4, -17, 2, 74, 89, 70, 254, -44, 89, -5, 74], self.speed_slow)
        self.piper_arm_right.run_piper_movement([37, 30, -10, -4, -17, 2, gripper_close, 89, 70, 254, -44, 89, -5, gripper_close], self.speed_slow)

        # 3 Shaking funnel carrier
        self.piper_arm_right.run_move_linear_known([89, 70, 254 + movement_z, -44, 89, -5, gripper_close], self.speed_fast)
        self.piper_arm_right.run_move_linear_known([89, 70, 254 + (movement_z/2), -44, 89, -5, gripper_close], self.speed_fast)
        self.piper_arm_right.run_move_linear_known([89, 70, 254 + movement_z, -44, 89, -5, gripper_close], self.speed_fast)
        
        # self.piper_arm_right.run_piper_movement([37, 30, -10, -4, -17, 2, gripper_close, 89, 70, 254, -44, 89, -5, gripper_close], self.speed_default)
        # self.piper_arm_right.run_piper_movement([39, 54, -58, -1, 40, 2, gripper_close, 147, 119, 390, 179, 59, -143, gripper_close], self.speed_default)
        # self.piper_arm_right.run_piper_movement([37, 30, -10, -4, -17, 2, gripper_close, 89, 70, 254, -44, 89, -5, gripper_close], self.speed_default)

        # 4 return funnel carrier
        self.piper_arm_right.run_move_linear_known([89, 70, 254 + 10, -44, 89, -5, gripper_close], self.speed_slow)
        self.piper_arm_right.run_piper_movement([37, 30, -10, -4, -17, 2, gripper_close, 89, 70, 254, -44, 89, -5, gripper_close], self.speed_slow)
        self.piper_arm_right.run_piper_movement([37, 30, -10, -4, -17, 2, 60, 89, 70, 254, -44, 89, -5, 72], self.speed_slow)

        # 5 funnel carrier and return home
        self.piper_arm_right.run_piper_movement([37, 5, -11, 1, 10, 0, 72, 43, 34, 256, 52, 88, 90, 72], self.speed_slow)
        self.piper_arm_right.run_piper_movement([33, -2, -28, 1, 38, -1, 72, -2, 0, 310, -171, 88, -137, 72], self.speed_default)
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 76, 56, 0, 213, 0, 85, 0, 0], self.speed_default)

    def run_lohc_action_8(self):
        self.run_lohc_action_8_1()
        self.run_lohc_action_8_2()
    
    def run_rail_to_left(self):
        """
        This function contains motion for action X : moving rail to left

        Input : None
        Output : None
        """
        movement_z = 60
        movement_y = 345
        gripper_close = 0

        print("ActionRailLeft")
        self.piper_arm_right.run_move_joint([0, 0, 0, 0, 0, 0, 0])
        self.piper_arm_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])

        # 1 Initialization Position 
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], self.speed_default)
        self.piper_arm_right.run_piper_movement([-27, 31, -58, -11, 74, 3, 0, 31, -35, 393, -169, 48, 153, 0], self.speed_default)

        # 2 Grap bowl carrier
        self.piper_arm_right.run_piper_movement([-35, 69, -44, 1, 63, -33, 73, 156, -106, 245, -177, 7, 178, 73], self.speed_default)
        self.piper_arm_right.run_move_linear_known([156, -106, 245 - movement_z, -177, 7, 178, 73],self.speed_slow)
        self.piper_arm_right.run_move_linear_known([156, -106, 245 - movement_z, -177, 7, 178, gripper_close],self.speed_slow)

        # 3 Move bowl carrier to left and release it
        # Total move length = 715 - 25 = 690 / 2 = 345
        self.piper_arm_right.run_move_linear_known([156, -106 - movement_y, 245 - movement_z, -177, 7, 178, gripper_close],self.speed_default, time_out = 10)
        self.piper_arm_right.run_piper_movement([-72, 118, -109, 4, 70, -72, 72, 142, -419, 272, -166, 8, -180, 72],self.speed_slow)

        # 4 Return right arm 
        self.piper_arm_right.run_piper_movement([-27, 31, -58, -11, 74, 3, 0, 31, -35, 393, -169, 48, 153, 73], self.speed_default)
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], self.speed_default)

        # 5 Initialization Position - left
        self.piper_arm_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])
        self.piper_arm_left.run_piper_movement([69, 119, -99, -1, 70, 71, -1, 152, 399, 217, 176, 2, 178, -1])
        
        # 6 Grap bowl carrier - left
        self.piper_arm_left.run_piper_movement([68, 122, -99, 1, 68, 73, 0, 158, 404, 191, 176, 0, 175, 0])
        self.piper_arm_left.run_move_linear_known([158, 404 - movement_y, 191, 176, 0, 175, 0], time_out = 10)
        self.piper_arm_left.run_move_linear_known([158, 404 - movement_y - 30, 191, 176, 0, 175, 0])


        # 7 Move bowl carrier to left and release it - left
        self.piper_arm_left.run_move_linear_known([158, 404 - movement_y - 30, 191, 176, 0, 175, 0], time_out = 10)
        self.piper_arm_left.run_move_linear_known([158, 404 - movement_y - 30, 191, 176, 0, 175, 0])

        # 8 Return left arm
        self.piper_arm_left.run_piper_movement([22, 36, -32, -1, 56, 23, 0, 90, 34, 275, 166, 33, 175, 0])
        self.piper_arm_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])
    
    def run_rail_to_right(self):
        """
        This function contains motion for action X : moving rail to right
        #WIP#

        Input : None
        Output : None
        """
        movement_z = 60
        movement_y = 345
        gripper_close = 0

        print("ActionRailRight")

        # 1 Initialize left arms
        self.piper_arm_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])
        self.piper_arm_left.run_piper_movement([36, 44, -38, 0, 59, -3, 0, 98, 71, 283, -179, 30, -141, 0])
        self.piper_arm_left.run_piper_movement([32, 72, -44, 0, 67, 31, 74, 161, 101 - 5, 237, 180, 1, -178, 74])

        # 2 Move carrier to right and release it
        self.piper_arm_left.run_move_linear_known([161, 101 - 5, 237 - movement_z, 180, 1, -178, 74])
        self.piper_arm_left.run_move_linear_known([161, 101 - 5 , 237 - movement_z, 180, 1, -178, gripper_close], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([161, 101 + movement_y + 20, 237 - movement_z, 180, 1, -178, gripper_close], time_out = 10)

        self.piper_arm_left.run_move_linear_known([161, 101 + movement_y, 237 - movement_z, 180, 1, -178, 74])
        self.piper_arm_left.run_piper_movement([69, 111, -102, 1, 70, 69, 62, 145, 387, 289, 165, 5, 179, 62], self.speed_slow)

        # 3 Return left arm
        self.piper_arm_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])

        # 4 Initialize right arms
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])
        self.piper_arm_right.run_piper_movement([-67, 118, -102, -9, 63, -64, 0, 159, -413, 242, -162, -1, 180, 0])
        
        # 5 Grap carrier and move it to right
        self.piper_arm_right.run_piper_movement([-71, 126, -105, 0, 65, -71, 0, 146, -434, 207, -169, 4, 180, 0])
        self.piper_arm_right.run_move_linear_known([146, -434 + movement_y + 50, 207, -169, 4, 180, 0], time_out = 10)

        # 6 Return right arm
        self.piper_arm_right.run_piper_movement([-13, 36, -34, -9, 55, -9, 0, 93, -34, 285, -162, 36, -176, 0])
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])

    def run_lohc_action_6(self):
        """
        This function contains motion for action 6 : Shaking bowl

        Input : None
        Output : None
        """
        movement_z = 80
        gripper_close = 0

        print("Action 6")

        # 1 Initialize arm
        self.piper_arm_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])
        self.piper_arm_left.run_piper_movement([36, 44, -38, 0, 59, -3, 0, 98, 71, 283, -179, 30, -141, 0])
        self.piper_arm_left.run_piper_movement([32, 72, -44, 0, 67, 31, 74, 161, 96, 237, 180, 1, -178, 74])

        # 2 grap bowl carrier and move it to shaker zone
        self.pa.run_digital_write(self.railmagnet, False)
        self.piper_arm_left.run_move_linear_known([161, 96, 237 - movement_z, 180, 1, -178, 74])
        self.piper_arm_left.run_move_linear_known([161, 96, 237 - movement_z, 180, 1, -178, gripper_close], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([161, 96, 237 + movement_z, 180, 1, -178, gripper_close], self.speed_slow)
        

        # 3 shaking bowl carrier by nearly not hitting it
        self.piper_arm_left.run_move_joint([0, 65, -63, 1, 70, 7, gripper_close])

        self.piper_arm_left.run_move_joint([0, 65, -83, 1, 70, 7, gripper_close], self.speed_fast)
        time.sleep(2)
        self.piper_arm_left.run_move_joint([0, 65, -58, 1, 70, 7, gripper_close], self.speed_fast)

        self.piper_arm_left.run_move_joint([0, 65, -83, 1, 70, 7, gripper_close], self.speed_fast)
        time.sleep(2)
        self.piper_arm_left.run_move_joint([0, 65, -58, 1, 70, 7, gripper_close], self.speed_fast)

        self.piper_arm_left.run_move_joint([0, 65, -83, 1, 70, 7, gripper_close], self.speed_fast)
        time.sleep(2)
        self.piper_arm_left.run_move_joint([0, 65, -58, 1, 70, 7, gripper_close], self.speed_fast)

        self.piper_arm_left.run_move_joint([0, 65, -63, 1, 70, 7, gripper_close])
   
        # 4 return bowl carrier
        self.pa.run_digital_write(self.railmagnet, True)
        self.piper_arm_left.run_move_joint([32, 65, -63, 1, 70, 7, gripper_close])
        self.piper_arm_left.run_piper_movement([32, 72, -44, 0, 67, 31, gripper_close, 161, 96, 237, 180, 1, -178, gripper_close])
        self.piper_arm_left.run_move_linear_known([161, 96, 237 - movement_z, 180, 1, -178, gripper_close], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([161, 96 - 10, 237 - movement_z, 180, 1, -178, gripper_close], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([161, 96 - 10, 237 - movement_z, 180, 1, -178, 80], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([161, 96 - 10, 237, 180, 1, -178, 80], self.speed_slow)

        # 5 Return robot arm
        self.piper_arm_left.run_piper_movement([32, 72, -44, 0, 67, 31, 74, 161, 101, 237, 180, 1, -178, 74],self.speed_slow)
        self.piper_arm_left.run_piper_movement([36, 44, -38, 0, 59, -3, 0, 98, 71, 283, -179, 30, -141, 0])
        self.piper_arm_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])
    
    def run_lohc_action_4(self):
        """
        This function contains motion for action 4 : Grinding bowl

        Input : None
        Output : None
        """
        movement_z = 80
        movement_y = 65
        gripper_close = 0

        movement_swing = 20
        print("Action4")

        def _grinding_action():
            self.piper_arm_left.run_piper_movement([18, 40, -12, -3, -31, 0, gripper_close, 148, 52, 247, -98, 87, -78, gripper_close])

            # First
            print("1")
            self.piper_arm_left.run_move_joint([23, 54, -5, 4, -30, -7, gripper_close])
            self.piper_arm_left.run_move_joint([23, 54, -5, 4, -30, -7 + movement_swing, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([23, 54, -5, 4, -30, -7 - movement_swing, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([23, 54, -5, 4, -30, -7, gripper_close], self.speed_default)

            self.piper_arm_left.run_move_joint([18, 40, 0, -3, -57, 0, gripper_close])

            # Second
            print("2")
            self.piper_arm_left.run_move_joint([18, 69, 0, -3, -57, 0, gripper_close])
            self.piper_arm_left.run_move_joint([18, 69, 0, -3, -57, 0 + movement_swing, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([18, 69, 0, -3, -57, 0 - movement_swing, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([18, 69, 0, -3, -57, 0, gripper_close], self.speed_default)

            # self.piper_arm_left.run_piper_movement([18, 40, -12, -3, -31, 0, gripper_close, 148, 52, 247, -98, 87, -78, gripper_close])

            self.piper_arm_left.run_move_joint([21, 69, 0, -3, -57, 0, gripper_close])
            # self.piper_arm_left.run_move_joint([23, 69, 0, -3, -57, 0 + movement_swing - movement_swing_cali, gripper_close])
            self.piper_arm_left.run_move_joint([21, 69, 0, -3, -57, 0 - movement_swing, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([21, 69, 0, -3, -57, 0, gripper_close], self.speed_default)

            # self.piper_arm_left.run_piper_movement([18, 40, -12, -3, -31, 0, gripper_close, 148, 52, 247, -98, 87, -78, gripper_close])
        
            # Third
            print("3")
            self.piper_arm_left.run_move_joint([23, 65, -4, 2, -48, -6, gripper_close])
            self.piper_arm_left.run_move_joint([23, 66, -4, 2, -48, -6 + movement_swing, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([23, 65, -4, 2, -48, -6 - movement_swing, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([23, 65, -4, 2, -48, -6, gripper_close], self.speed_default)

            # self.piper_arm_left.run_piper_movement([18, 40, -12, -3, -31, 0, gripper_close, 148, 52, 247, -98, 87, -78, gripper_close])

            self.piper_arm_left.run_move_joint([18, 65, -4, 2, -48, -6, gripper_close])
            self.piper_arm_left.run_move_joint([18, 66, -4, 2, -48, -6 + movement_swing, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([18, 65, -4, 2, -48, -6 - movement_swing, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([18, 65, -4, 2, -48, -6, gripper_close], self.speed_default)

            # self.piper_arm_left.run_piper_movement([18, 40, -12, -3, -31, 0, gripper_close, 148, 52, 247, -98, 87, -78, gripper_close])

            # Forth
            print("4")
            self.piper_arm_left.run_move_joint([18, 75, -3, 2, -61, 0, gripper_close])
            self.piper_arm_left.run_move_joint([18, 75, -3, 2, -61, 0 + movement_swing, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([18, 75, -3, 2, -61, 0 - movement_swing, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([18, 75, -3, 2, -61, 0, gripper_close], self.speed_default)

            # self.piper_arm_left.run_piper_movement([18, 40, -12, -3, -31, 0, gripper_close, 148, 52, 247, -98, 87, -78, gripper_close])

            self.piper_arm_left.run_move_joint([23, 75, -3, 2, -61, 0, gripper_close])
            # self.piper_arm_left.run_move_joint([23, 75, -3, 2, -61, 0 + movement_swing - movement_swing_cali, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([23, 75, -3, 2, -61, 0 - movement_swing, gripper_close], self.speed_default)
            self.piper_arm_left.run_move_joint([23, 75, -3, 2, -61, 0, gripper_close], self.speed_default)

            self.piper_arm_left.run_piper_movement([18, 40, -12, -3, -31, 0, gripper_close, 148, 52, 247, -98, 87, -78, gripper_close])

        # 1 Initialize arm
        self.piper_arm_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])
        self.piper_arm_left.run_piper_movement([-2, 22, -34, 0, 19, -4, 74, 75, -3, 357, -114, 86, -116, 74])
        self.piper_arm_left.run_piper_movement([92, 73, -36, 2, -32, -1, 74, -9, 269, 291, -91, 90, 0, 74])
        
        # 2 Grap macja
        self.piper_arm_left.run_move_linear_known([-9, 269 + movement_y, 291, -91, 90, 0, 74], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([-9, 269 + movement_y, 291, -91, 90, 0, gripper_close])
        self.piper_arm_left.run_piper_movement([92, 80, -62, 3, -13, -3, gripper_close, -9, 269 + movement_y, 291 + movement_z, -91, 90, 0, gripper_close], self.speed_slow)
        
        # 3 Do grinding
        self.piper_arm_left.run_piper_movement([53, 52, -57, -3, 21, -1, gripper_close, 115, 150, 417, -159, 78, -107, gripper_close])
    
        for i in range(1):
            _grinding_action()
        
        self.piper_arm_left.run_piper_movement([53, 52, -57, -3, 21, -1, gripper_close, 115, 150, 417, -159, 78, -107, gripper_close])

        # 4 Return macja
        self.piper_arm_left.run_piper_movement([92, 80, -62, 3, -13, -3, gripper_close, -9, 269 + movement_y - 7, 291 + movement_z, -91, 90, 0, gripper_close])
        self.piper_arm_left.run_move_linear_known([-9, 269 + movement_y - 7, 291, -91, 90, 0, gripper_close], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([-9, 269 + movement_y - 7, 291, -91, 90, 0, 74])
        self.piper_arm_left.run_move_linear_known([-9, 269 - movement_y - 7, 291, -91, 90, 0, 74], self.speed_slow)

        # 5 Return arm
        self.piper_arm_left.run_piper_movement([-2, 22, -34, 0, 19, -4, 74, 75, -3, 357, -114, 86, -116, 74])
        self.piper_arm_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])

    def run_test(self):
        """
        This function contains test curve motions.

        Input : None
        Output : None
        """
        self.piper_arm_left.run_move_curve([
            [60, 0, 250, 0, 85, 0, 0x01], # 출발점
            [200, 0, 400, 0, 85, 0, 0x02], # 경유점
            [60, 0, 550, 0, 85, 0, 0x03], # 도착점
            ])
        time.sleep(15)
        self.piper_arm_left.run_move_curve([
            [60, 0, 550, 0, 85, 0, 0x01], # 출발점
            [200, 0, 400, 0, 85, 0, 0x02], # 경유점
            [60, 0, 250, 0, 85, 0, 0x03], # 도착점
            ])
        time.sleep(15)

    def run_pippet_init(self):
        # 1) Getting in menu
        self.p2c.run_serial_command("button", "TRIGGER_BUTTON_POWER")
 
        for i in range(4):
            self.p2c.run_serial_command("button", "DOWN")
 
        self.p2c.run_serial_command("button", "TRIGGER_BUTTON_TOP")

        # 2) Start 20 dispensing mode - charge liquid
        self.p2c.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        time.sleep(4)
        
        self.p2c.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        print("Prep Complete")

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
        speed_slow = 15
        speed_default = 70
        speed_fast = 90

        

        # 1. Set Pose

        self.piper_arm_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])
        self.piper_arm_left.run_piper_movement([0, 20, -32, -1, 19, -3, 0, 74, 1, 347, -108, 86, -107, 74], speed_default)

        self.piper_arm_left.run_move_joint([90, 20, -32, -1, 19, -3, 0, 74])
        self.piper_arm_left.run_move_joint([140, 20, -32, -1, 19, -3, 0, 74])
        self.piper_arm_left.run_move_joint([140, 20, -32, 93, 19, -3, 0, 74])
        self.piper_arm_left.run_move_joint([140, 20, -32, 93, 19, -3, 0, 74])
        self.piper_arm_left.run_piper_movement([133, 96, -39, 50, -66, -25, 71, -158, 266, 221, 53, 86, 140, 74], speed_default)

        # 2. Approach target

        self.piper_arm_left.run_piper_movement([133, 96, -39, 50, -66, -25, 71, -158, 266, 221, 53, 86, 140, 74], speed_slow)
        self.piper_arm_left.run_move_linear_known([-158, 269 + movement_y, 221, -91, 90, 0, 74], speed_default)
        self.piper_arm_left.run_move_linear_known([-158, 269 + movement_y, 221, -91, 90, 0, 74])

         # 3. Escpae
        
        self.piper_arm_left.run_move_linear_known([-158, 333, 221 + movement_z, -91, 90, 0, gripper_close], speed_default)
        self.piper_arm_left.run_move_linear_known([-158, 333, 221 + movement_z, -91, 90, 0, gripper_close])

        self.piper_arm_left.run_move_linear_known([-158, 333 - movement_y, 395, -91, 90, 0, gripper_close], speed_default)
        self.piper_arm_left.run_move_linear_known([-158, 333 - movement_y, 395, -91, 90, 0, gripper_close])
        self.piper_arm_left.run_move_linear_known([-158, 150, 395, -91, 90, 0, gripper_close], speed_default)
        self.piper_arm_left.run_move_linear_known([81, 110, 395, 65, 89, 119, gripper_close], speed_default)

        # # 4. Pippeting 
        self.piper_arm_left.run_piper_movement([18, 42, -43, 1, 0, 1, gripper_close, 147, 47, 399, 19, 83, 37, gripper_close], speed_default)

        self.piper_arm_left.run_piper_movement([19, 42, -24, -2, -11, 4, gripper_close, 148, 53, 303, 138, 87, 158, gripper_close]) # 5
        self.p2c.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        time.sleep(wait)

        self.piper_arm_left.run_move_linear_known([148 + distance, 53 + distance, 303, 138, 87, 158, gripper_close], speed_slow) # 1
        self.p2c.run_serial_command("button", "TRIGGER_BUTTON_TOP")
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
        self.piper_arm_left.run_move_linear_known([148, 53, 303, 138, 87, 158, gripper_close], speed_slow) # 5
        time.sleep(wait)

        # # inverse replay
        self.piper_arm_left.run_piper_movement([18, 42, -43, 1, 0, 1, gripper_close, 147, 47, 399, 19, 83, 37, gripper_close], speed_fast)

        # self.piper_arm_left.run_move_linear_known([81, 110, 395, 65, 89, 119, gripper_close], self.speed_fast)
        self.piper_arm_left.run_piper_movement([107, 39, -44, 100, -46, -104, gripper_close, 28, 125, 396, -62, 90, 0, gripper_close])
        self.piper_arm_left.run_piper_movement([150, 68, -57, 86, -59, -83, gripper_close, -158, 181, 395, -91, 90, 0, gripper_close])
        self.piper_arm_left.run_move_linear_known([-158, 181 + movement_y, 395, -91, 90, 0, gripper_close], self.speed_default)
        self.piper_arm_left.run_move_linear_known([-158, 181 + movement_y, 395, -91, 90, 0, gripper_close])
        self.piper_arm_left.run_move_linear_known([-158, 337, 395, -91, 90, 0, gripper_close]) #y=335

        self.piper_arm_left.run_move_linear_known([-158, 330, 395 - movement_z, -91, 90, 0, gripper_close], speed_default)
        self.piper_arm_left.run_move_linear_known([-158, 330, 395 - movement_z, -91, 90, 0, gripper_close])
        self.piper_arm_left.run_move_linear_known([-158, 330, 221, -91, 90, 0, 74]) #330

        
        self.piper_arm_left.run_move_linear_known([-158, 332 - movement_y, 221, -91, 90, 0, 74], speed_slow)
        self.piper_arm_left.run_move_linear_known([-158, 332 - movement_y, 221, -91, 90, 0, 74])
        self.piper_arm_left.run_move_linear_known([-158, 256, 221, -91, 90, 0, 74], speed_slow)
        self.piper_arm_left.run_piper_movement([133, 96, -39, 50, -66, -25, 71, -158, 266, 221, 53, 86, 140, 74], speed_slow)

        self.piper_arm_left.run_piper_movement([133, 96, -39, 50, -66, -25, 71, -158, 266, 221, 53, 86, 140, 74], speed_default)
        self.piper_arm_left.run_move_joint([140, 20, -32, 93, 19, -3, 0, 74], speed_default)
        self.piper_arm_left.run_move_joint([140, 20, -32, 93, 19, -3, 0, 74])
        self.piper_arm_left.run_move_joint([140, 20, -32, -1, 19, -3, 0, 74])
        self.piper_arm_left.run_move_joint([90, 20, -32, -1, 19, -3, 0, 74])
        
        self.piper_arm_left.run_piper_movement([0, 20, -32, -1, 19, -3, 0, 74, 1, 347, -108, 86, -107, 74], speed_default)
        self.piper_arm_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])

    def run_scenario(self):
        cycle_pippet = 10
        cycle_grinding = 5

        self.run_lohc_action_1()
        self.run_rail_to_left()
        self.run_pippet_init()
        for i in range(cycle_pippet):
            self.run_lohc_action_3
            print("cycle_pippet :"  + str(i))

            for j in range(cycle_grinding):
                self.run_lohc_action_4()
                self.run_lohc_action_6()
                print("cycle_grinding :"  + str(j))

        self.run_rail_to_left
        self.run_lohc_action_8()

if __name__ == "__main__":
    lab = LOHCActionBook()
    # lab.run_pippet_init()
    for i in range(1):
        # lab.run_lohc_action_1() #shinyoung
        # lab.run_rail_to_left() #me
        # lab.run_lohc_action_3() #shinyoung
        # lab.run_lohc_acti
        # on_4() #me
        # lab.run_lohc_action_6() #me
        # lab.run_rail_to_right() #me
        lab.run_lohc_action_8() #me
        # lab.run_test()