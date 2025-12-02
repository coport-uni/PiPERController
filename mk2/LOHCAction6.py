from PiPERControllerMK2 import PiPERControllerMK2
from piper_sdk import *
import time

def main():
    piper_right = PiPERControllerMK2(C_PiperInterface("piper_right"))

    speed_default = 20

    print("Action 6")
    piper_right.run_move_joint([0, 0, 0, 0, 0, 0, 0])

    # 1 Initialization Position 
    piper_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], speed_default)
    piper_right.run_piper_movement([30, 69, -41, 1, 63, 33, 0, 156, 93, 233, 177, 3, 177, 0], speed_default)
    piper_right.run_piper_movement([33, 20, -41, 1, 63, 33, 0, 30, 22, 331, 143, 42, 166, 0], speed_default)


if __name__ == "__main__":
    for i in range(3):
        main()