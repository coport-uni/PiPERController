from PiPERControllerMK2 import PiPERControllerMK2
from piper_sdk import *
import time

def main():
    piper_left = PiPERControllerMK2(C_PiperInterface("piper_left"))

    speed_default = 20
    speed_fast = 90

    gripper_zmove = 60
    gripper_close = 40

    movement_y = 200

    print("Action 6")
    piper_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])

    # filepath = "/home/sungwoo/workspace/PiPERController/mk2/action_record/action4.csv"
    # piper_left.run_record_csv(filepath)

    # for softer motion

    # 1 Initialization Position 
    piper_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], speed_default)

    # # 2 Close to rail and grap it
    # # origin_position  = [30, 72, -42, -3, 60, 31, 75, 169, 94, 225, 180, 5, -179, 75]
    # piper_left.run_piper_movement([31, 70, -41, -4, 60, 35, 74, 164, 90, 229, -180, 7, 178, 74], speed_default)
    # piper_left.run_move_linear_known([169, 94, 225 - 60, 180, 5, -179, 75], speed_default)
    # piper_left.run_move_linear_known([169, 94, 225 - 60, 180, 5, -179, 75 - 25], speed_default)

    # # 3 Move the rail to Y positive and return for 2 times
    # piper_left.run_move_linear_known([169, 94, 225 - 60, 180, 5, -179, 75 - 25], speed_fast)
    # piper_left.run_move_linear_known([169, 94 + 200, 225 - 60, 180, 5, -179, 75 - 25], speed_fast)

    # piper_left.run_move_linear_known([169, 94, 225 - 60, 180, 5, -179, 75 - 25], speed_fast)
    # piper_left.run_move_linear_known([169, 94 + 200, 225 - 60, 180, 5, -179, 75 - 25], speed_fast)

    # piper_left.run_move_linear_known([169, 94, 225 - 60, 180, 5, -179, 75 - 25], speed_fast)
    # piper_left.run_move_linear_known([169, 94 + 200, 225 - 60, 180, 5, -179, 75 - 25], speed_fast)

    # piper_left.run_move_linear_known([169, 94, 225 - 60, 180, 5, -179, 75 - 25], speed_fast)

    # # X Return Position
    # piper_left.run_move_linear_known([169, 94, 225 + 60, 180, 5, -179, 75], speed_default)
    # piper_left.run_piper_movement([31, 30, -53, -3, 71, 22, 92, 46, 22, 373, 162, 44, -179, 92], speed_default) 
    # piper_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], speed_default)

    # 2 Close to rail and grap it
    origin_position = [31, 71, -41, -5, 62, 36, 76, 164, 89, 226, -178, 5, 177, 76]
    piper_left.run_piper_movement([31, 71, -41, -5, 62, 36, 76, 164, 89, 226, -178, 5, 177, 76], speed_default)
    piper_left.run_move_linear_known([164, 89, 226 - gripper_zmove, -178, 5, 177, 76], speed_default)
    piper_left.run_move_linear_known([164, 89, 226 - gripper_zmove, -178, 5, 177, gripper_close], speed_default)

    # 3 Move the rail to Y positive and return for 2 times
    piper_left.run_move_linear_known([164, 89, 226 - gripper_zmove, -178, 5, 177, gripper_close], speed_fast)
    piper_left.run_move_linear_known([164, 89 + movement_y, 226 - gripper_zmove, -178, 5, 177, gripper_close], speed_fast)
    piper_left.run_move_linear_known([164, 89, 226 - gripper_zmove, -178, 5, 177, gripper_close], speed_fast)

    piper_left.run_move_linear_known([164, 89, 226 - gripper_zmove, -178, 5, 177, gripper_close], speed_fast)
    piper_left.run_move_linear_known([164, 89 + movement_y, 226 - gripper_zmove, -178, 5, 177, gripper_close], speed_fast)
    piper_left.run_move_linear_known([164, 89, 226 - gripper_zmove, -178, 5, 177, gripper_close], speed_fast)

    # 4 Release it and return Position
    piper_left.run_move_linear_known([164, 89, 226, -178, 5, 177, 75], speed_default)
    piper_left.run_move_linear_known([164, 89, 226 + gripper_zmove, -178, 5, 177, 75], speed_default)
    piper_left.run_piper_movement([31, 30, -53, -3, 71, 22, 92, 46, 22, 373, 162, 44, -179, 92], speed_default) 
    piper_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], speed_default)


if __name__ == "__main__":
    for i in range(3):
        main()