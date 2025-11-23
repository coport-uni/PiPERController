from PiPERControllerMK2 import PiPERControllerMK2
from piper_sdk import *
import time

def main():
    piper_left = PiPERControllerMK2(C_PiperInterface("piper_left"))

    print("Action 4")
    piper_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])

    # filepath = "/home/sungwoo/workspace/PiPERController/mk2/action_record/action4.csv"
    # piper_left.run_record_csv(filepath)

    # for softer motion

    # 1 Initialization Position 
    piper_left.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0])

    # 2 Close to macja and grap it
    piper_left.run_piper_movement([86, 109, -25, -4, -77, 1, 96, 16, 288, 133, 170, 88, -100, 96])
    piper_left.run_move_linear_known([18, 253 + 30 , 104, 178, 73, -94, 98])




if __name__ == "__main__":
    main()