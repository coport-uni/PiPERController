from PiPERControllerMK2 import PiPERControllerMK2
from piper_sdk import *
from PyArduino import PyArduino
import time

class LOHCActionBook():
    def __init__(self):
        self.pa = PyArduino()

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
        movement_z = 100
        gripper_close = 0

        print("Action 8")
        self.piper_arm_right.run_move_joint([0, 0, 0, 0, 0, 0, 0])

        # 1 Initialization Position 
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], self.speed_default)
        self.piper_arm_right.run_piper_movement([33, -2, -28, 1, 38, -1, -2, -2, 0, 310, -171, 88, -137, -2], self.speed_default)
        self.piper_arm_right.run_piper_movement([37, 5, -11, 1, 10, 0, 72, 43, 34, 256, 52, 88, 90, 72], self.speed_slow)

        # 2 Grap funnel carrier
        self.piper_arm_right.run_piper_movement([37, 30, -10, -4, -17, 2, 60, 89, 70, 254, -44, 89, -5, 72], self.speed_slow)
        self.piper_arm_right.run_piper_movement([37, 30, -10, -4, -17, 2, gripper_close, 89, 70, 254, -44, 89, -5, gripper_close], self.speed_slow)

        # 3 Shaking funnel carrier
        self.piper_arm_right.run_move_linear_known([89, 70, 254 + movement_z, -44, 89, -5, gripper_close], self.speed_fast)
        self.piper_arm_right.run_move_linear_known([89, 70, 254 + (movement_z/2), -44, 89, -5, gripper_close], self.speed_fast)
        self.piper_arm_right.run_move_linear_known([89, 70, 254 + movement_z, -44, 89, -5, gripper_close], self.speed_fast)
        
        # self.piper_arm_right.run_piper_movement([37, 30, -10, -4, -17, 2, gripper_close, 89, 70, 254, -44, 89, -5, gripper_close], self.speed_default)
        # self.piper_arm_right.run_piper_movement([39, 54, -58, -1, 40, 2, gripper_close, 147, 119, 390, 179, 59, -143, gripper_close], self.speed_default)
        # self.piper_arm_right.run_piper_movement([37, 30, -10, -4, -17, 2, gripper_close, 89, 70, 254, -44, 89, -5, gripper_close], self.speed_default)

        # 4 return funnel carrier
        self.piper_arm_right.run_move_linear_known([89, 70, 254, -44, 89, -5, gripper_close], self.speed_slow)
        self.piper_arm_right.run_move_linear_known([86, 67, 254, -44, 89, -5, gripper_close], self.speed_slow)

        # 5 funnel carrier and return home
        self.piper_arm_right.run_piper_movement([37, 5, -11, 1, 10, 0, 72, 43, 34, 256, 52, 88, 90, 72], self.speed_slow)
        self.piper_arm_right.run_piper_movement([33, -2, -28, 1, 38, -1, 72, -2, 0, 310, -171, 88, -137, 72], self.speed_default)
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 76, 56, 0, 213, 0, 85, 0, 76], self.speed_default)

    def run_rail_to_left(self):
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
        self.piper_arm_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 73], self.speed_default)

        # 5 Initialization Position - left
        self.piper_arm_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])
        self.piper_arm_left.run_piper_movement([23, 32, -46, -6, 73, 26, 0, 62, 17, 336, 167, 35, 172, 0])

        # 6 Grap bowl carrier - left
        self.piper_arm_left.run_piper_movement([77, 119, -102, -13, 65, 80, 80, 120, 426, 233, 170, 15, 179, 80])
        self.piper_arm_left.run_piper_movement([74, 134, -113, -7, 73, 75, 63, 139, 452, 164, -179, 7, -179, 63],self.speed_slow)
        self.piper_arm_left.run_piper_movement([74, 134, -113, -7, 73, 75, gripper_close, 139, 452, 164, -179, 7, -179, gripper_close],self.speed_slow)

        # 7 Move bowl carrier to left and release it - left
        self.piper_arm_left.run_move_linear_known([139, 452 - movement_y + 10, 164, -179, 7, -179, gripper_close], time_out = 10)
        self.piper_arm_left.run_move_linear_known([139, 452 - movement_y - 13, 164, -179, 7, -179, gripper_close])
        self.piper_arm_left.run_move_linear_known([139, 452 - movement_y - 13, 164 + movement_z + 20, -179, 7, -179, 80], self.speed_slow)

        # 8 Return left arm 
        self.piper_arm_left.run_piper_movement([23, 32, -46, -6, 73, 26, 0, 62, 17, 336, 167, 35, 172, 0])
        self.piper_arm_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])
    
    def run_rail_to_right(self):
        print("ActionRailRight")

    def run_shaking(self):

        movement_z = 80
        gripper_close = 0

        print("shaking")

        # 1 Initialize arm
        self.piper_arm_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])
        self.piper_arm_left.run_piper_movement([36, 44, -38, 0, 59, -3, 0, 98, 71, 283, -179, 30, -141, 0])
        self.piper_arm_left.run_piper_movement([32, 72, -44, 0, 67, 31, 74, 161, 101, 237, 180, 1, -178, 74])

        # 2 grap bowl carrier and move it to shaker zone
        self.pa.run_digital_write(self.railmagnet, False)
        self.piper_arm_left.run_move_linear_known([161, 101, 237 - movement_z, 180, 1, -178, 74])
        self.piper_arm_left.run_move_linear_known([161, 101, 237 - movement_z, 180, 1, -178, gripper_close], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([161, 101, 237 + movement_z, 180, 1, -178, gripper_close], self.speed_slow)
        

        # 3 shaking bowl carrier by nearly hitting it
        self.piper_arm_left.run_piper_movement([96, 65, -63, 1, 70, 7, gripper_close, -22, 199, 347, 176, 23, -92, gripper_close])

        self.piper_arm_left.run_move_joint([96, 65, -83, 1, 70, 7, gripper_close], self.speed_fast)
        self.piper_arm_left.run_move_joint([96, 65, -58, 1, 70, 7, gripper_close], self.speed_fast)

        self.piper_arm_left.run_move_joint([96, 65, -83, 1, 70, 7, gripper_close], self.speed_fast)
        self.piper_arm_left.run_move_joint([96, 65, -58, 1, 70, 7, gripper_close], self.speed_fast)

        self.piper_arm_left.run_move_joint([96, 65, -83, 1, 70, 7, gripper_close], self.speed_fast)
        self.piper_arm_left.run_move_joint([96, 65, -58, 1, 70, 7, gripper_close], self.speed_fast)

        self.piper_arm_left.run_piper_movement([96, 65, -63, 1, 70, 7, gripper_close, -22, 199, 347, 176, 23, -92, gripper_close])
   
        # 4 return bowl carrier
        self.pa.run_digital_write(self.railmagnet, True)
        self.piper_arm_left.run_move_joint([32, 65, -63, 1, 70, 7, gripper_close])
        self.piper_arm_left.run_piper_movement([32, 72, -44, 0, 67, 31, gripper_close, 161, 101, 237, 180, 1, -178, gripper_close])
        self.piper_arm_left.run_move_linear_known([161, 101, 237 - movement_z, 180, 1, -178, gripper_close], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([161, 101 - 10, 237 - movement_z, 180, 1, -178, gripper_close], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([161, 101 - 10, 237 - movement_z, 180, 1, -178, 80], self.speed_slow)
        self.piper_arm_left.run_move_linear_known([161, 101 - 10, 237, 180, 1, -178, 80], self.speed_slow)

        # 5 Return robot arm
        self.piper_arm_left.run_piper_movement([32, 72, -44, 0, 67, 31, 74, 161, 101, 237, 180, 1, -178, 74],self.speed_slow)
        self.piper_arm_left.run_piper_movement([36, 44, -38, 0, 59, -3, 0, 98, 71, 283, -179, 30, -141, 0])
        self.piper_arm_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])
        
        
if __name__ == "__main__":
    lab = LOHCActionBook()
    for i in range(3):
        # lab.run_lohc_action_8_1()
        # lab.run_lohc_action_8_2()
        # lab.run_rail_to_left()
        # lab.run_rail_to_right()
        lab.run_shaking()