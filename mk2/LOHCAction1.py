from PiPERControllerMK2 import PiPERControllerMK2
from piper_sdk import *
import time

def main():
    piper_left = PiPERControllerMK2(C_PiperInterface("piper_left"))

    speed_slow = 10
    speed_default = 20
    speed_fast = 90

    gripper_close = 40

    print("Action 1")
    piper_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])

    # filepath = "/home/sungwoo/workspace/PiPERController/mk2/action_record/action4.csv"
    # piper_left.run_record_csv(filepath)

    # for softer motion

    # 1 Initialization Position 
    piper_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], speed_default)
    piper_left.run_piper_movement([87, -3, -41, 2, 50, -3, 76, -4, -43, 347, -134, 87, -46, 76], speed_default)

    # 2 Close bottle and grap it
    origin_position = [79, 4, -25, 17, 26, -22, 76, -7, 29, 310, -85, 84, 2, 76]
    piper_left.run_piper_movement([79, 4, -25, 17, 26, -22, 76, -7, 29, 310, -85, 84, 2, 76], speed_default)

    piper_left.run_piper_movement([91, 18, -24, -2, 14, 0, 76, 0, 77, 310, -141, 86, -51, 76], speed_slow)
    piper_left.run_piper_movement([91, 18, -24, -2, 14, 0, gripper_close, 0, 77, 310, -141, 86, -51, gripper_close], speed_slow)
    piper_left.run_move_linear_known([0, 77, 310 + 100, -141, 86, -51, gripper_close], speed_slow)

    # Move to Macja
    piper_left.run_piper_movement([26, 29, -47, 2, 21, 4, gripper_close, 78, 39, 414, 73, 84, 100, gripper_close], speed_default)
    piper_left.run_piper_movement([-30, 40, -38, -4, 2, -1, gripper_close, 128, -73, 371, -77, 86, -107, -2], speed_default)
    piper_left.run_piper_movement([-20, 49, -22, -3, -36, 1, gripper_close, 163, -58, 309, -8, 76, -27, -3], speed_default)

    # Pour it with little pounding for 2 times
    piper_left.run_piper_movement([-28, 53, -6, -16, -42, 11, gripper_close, 142, -57, 222 + 75, -93, 89, -110, gripper_close], speed_default)
    piper_left.run_piper_movement([-14, 52, -18, 13, -11, 118, gripper_close, 167, -45, 242 + 75, 112, -37, 60, gripper_close], speed_slow, time_out = 5)
    time.sleep(2)
    piper_left.run_piper_movement([-14, 57, -23, 67, -13, 122, gripper_close, 180, -64, 244 + 75, -172, -67, -35, gripper_close], speed_slow, time_out = 5)
    time.sleep(2)
    piper_left.run_piper_movement([-14, 52, -18, 13, -11, 118, gripper_close, 167, -45, 242 + 75, 112, -37, 60, gripper_close], speed_slow, time_out = 5)
    time.sleep(2)

    piper_left.run_move_joint([-28, 53, -30, -16, -42, 11, gripper_close])

    piper_left.run_piper_movement([-28, 53, -6, -16, -42, 11, gripper_close, 142, -57, 222 + 75, -93, 89, -110, gripper_close], speed_default)
    piper_left.run_piper_movement([-14, 52, -18, 13, -11, 118, gripper_close, 167, -45, 242 + 75, 112, -37, 60, gripper_close], speed_slow, time_out = 5)
    time.sleep(2)
    piper_left.run_piper_movement([-14, 57, -23, 67, -13, 122, gripper_close, 180, -64, 244 + 75, -172, -67, -35, gripper_close], speed_slow, time_out = 5)
    time.sleep(2)
    piper_left.run_piper_movement([-14, 52, -18, 13, -11, 118, gripper_close, 167, -45, 242 + 75, 112, -37, 60, gripper_close], speed_slow, time_out = 5)
    time.sleep(2)

    piper_left.run_move_joint([-28, 53, -30, -16, -42, 11, gripper_close])

    # Move to stand
    piper_left.run_piper_movement([-20, 49, -22, -3, -36, 1, gripper_close, 163, -58, 309, -8, 76, -27, -3], speed_default)
    piper_left.run_piper_movement([-30, 40, -38, -4, 2, -1, gripper_close, 128, -73, 371, -77, 86, -107, -2], speed_default)
    piper_left.run_piper_movement([26, 29, -47, 2, 21, 4, gripper_close, 78, 39, 414, 73, 84, 100, gripper_close], speed_default)
    piper_left.run_move_linear_known([0, 77, 310 + 100, -141, 86, -51, gripper_close], speed_default, time_out = 15)

    # Release bottle and return
    piper_left.run_move_linear_known([0, 77, 310, -141, 86, -51, gripper_close], speed_default, time_out = 15)
    piper_left.run_piper_movement([91, 18, -24, -2, 14, 0, 76, 0, 77, 310, -141, 86, -51, 76], speed_slow)
    piper_left.run_piper_movement([79, 4, -25, 17, 26, -22, 76, -7, 29, 310, -85, 84, 2, 76], speed_default)

    piper_left.run_piper_movement([87, -3, -41, 2, 50, -3, 76, -4, -43, 347, -134, 87, -46, 76], speed_default)
    piper_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], speed_default)


if __name__ == "__main__":
    for i in range(1):
        main()