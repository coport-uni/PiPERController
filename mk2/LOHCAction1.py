from PiPERControllerMK2 import PiPERControllerMK2
from piper_sdk import *
import time

def main():
    piper_left = PiPERControllerMK2(C_PiperInterface("piper_left"))

    print("Action 1")
    piper_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])

    filepath = "/home/sungwoo/workspace/PiPERController/mk2/action_record/action1.csv"
    piper_left.run_record_csv(filepath)
    
    # while True:
    #     # HomePosition
    #     piper_left.run_piper_movement([-1, -2, 1, 0, 16, 6, 0, 53, -1, 185, 148, 79, 147, 0])

    #     # Turn -90 le
    #     piper_left.run_piper_movement([-92, -2, 1, 0, 16, 6, 0, -2, -53, 185, 148, 79, 56, 0])

    #     # Hover above and Below the arm
    #     piper_left.run_piper_movement([-91, 91, -51, -2, 53, 2, 94, -9, -265, 189, -179, 3, 87, 94])
    #     piper_left.run_piper_movement([-91, 91, -51, -2, 53, 2, 94, -9, -265, 166, -179, 3, 87, 94])
    
if __name__ == "__main__":
    main()