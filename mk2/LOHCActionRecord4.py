from PiPERControllerMK2 import PiPERControllerMK2
from piper_sdk import *
import time

def main():
    # bash can_activate.sh
    # bash can_activate.sh can0 1000000
    # bash can_activate.sh piper_left 1000000 "3-1:1.0"

    piper_left = PiPERControllerMK2(C_PiperInterface("piper_left"))
    filepath = "/home/sungwoo/workspace/PiPERController/mk2/action_record/action4.csv"

    while True:
        piper_left.get_record_csv(filepath, piper_left.get_joint_status(), piper_left.get_eef_status())
    
if __name__ == "__main__":
    main()