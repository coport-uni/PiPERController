from PiPERControllerMK2 import PiPERControllerMK2
from piper_sdk import *
import time

def main():
    piper_left = PiPERControllerMK2(C_PiperInterface("piper_left"))

    speed_slow = 10
    speed_default = 20
    speed_fast = 90

    gripper_move_y = 130
    gripper_close = 0
    
    movement_y = 200

    print("Action 4")
    piper_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])

    # filepath = "/home/sungwoo/workspace/PiPERController/mk2/action_record/action4.csv"
    # piper_left.run_record_csv(filepath)

    # for softer motion

    # 1 Initialization Position 
    piper_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, gripper_close], speed_default)

    # 2 Close to rail and grap it
    origin_position = [-86, 9, -36, -9, 32, 8, 58, -6, -20, 357, 91, 90, 0, 58]
    piper_left.run_piper_movement([-86, 9, -36, -9, 32, 8, 58, -6, -20, 357, 91, 90, 0, 100], speed_default)
    piper_left.run_move_linear_known([-6, -20 - gripper_move_y, 357, 91, 90, 0, 100], speed_slow)
    piper_left.run_move_linear_known([-6, -20 - gripper_move_y, 357, 91, 90, 0, 0], speed_slow)

    # x 
    piper_left.run_move_linear_known([-6, -20 - gripper_move_y, 357 + 100, 91, 90, 0, 0], speed_slow)
    piper_left.run_move_linear_known([-6, -20 - gripper_move_y, 357, 91, 90, 0, 0], speed_slow)
    

    # x Return to home position
    piper_left.run_move_linear_known([-6, -20 - gripper_move_y, 357, 91, 90, 0, 100], speed_slow)
    piper_left.run_move_linear_known([-6, -20 + gripper_move_y, 357, 91, 90, 0, 100], speed_slow)
    piper_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, gripper_close], speed_default)
    


if __name__ == "__main__":
    for i in range(3):
        main()