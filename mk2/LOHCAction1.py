from PiPERControllerMK2 import PiPERControllerMK2
from piper_sdk import *
import time

def main():
    piper_left = PiPERControllerMK2(C_PiperInterface("piper_left"))

    print("Action 1")
    piper_left.run_move_joint([0, 0, 0, 0, 0, 0, 0])

    filepath = "/home/sungwoo/workspace/PiPERController/mk2/action_record/action1.csv"
    piper_left.run_record_csv(filepath)
    
    
if __name__ == "__main__":
    main()