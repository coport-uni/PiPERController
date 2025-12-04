#!/usr/bin/env python3
# -*-coding:utf8-*-

from typing import Optional
from piper_sdk import *
from PiPERMover import PiPERMover
import time
import os
import csv
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

class PiPERControllerMK2:
    def __init__(self, piper:C_PiperInterface):
        # bash can_activate.sh
        # bash can_activate.sh can0 1000000
        # os.system(bash can_activate.sh piper_left 1000000 "3-1.2:1.0")
        # os.system(bash can_activate.sh piper_right 1000000 "3-1.3:1.0")
        # os.system("python3 piper_ctrl_reset.py")
        self.timeout = 3

        # os.system("bash can_activate.sh piper_right 1000000 \"3-1.3:1.0\"")
        # os.system("bash can_activate.sh piper_left 1000000 \"3-1.2:1.0\"")
        self.piper = piper
        self.piper.ConnectPort()
        self.piper_arm = PiPERMover(self.piper)
        self.piper_arm.enable.run()
        self.time_action = 0.01
        
    def run_move_joint(self, joint_list : list, speed=20):
        self.piper_arm.movej.run(*joint_list, speed = speed)
        time.sleep(self.time_action)

    def run_move_natural(self, eef_list : list):
        self.piper_arm.movep.run(*eef_list)
        time.sleep(self.time_action)
    
    # def run_move_linear_unknown(self, eef_list : list, speed : int):
        
    #     signal.signal(signal.SIGALRM, timeout_handler)
    #     signal.alarm(self.timeout)

    #     current_eef = self.get_eef_status()

    #     try:
    #         for i in range(7):
    #             action = current_eef
    #             action[i] = eef_list[i]
    #             self.piper_arm.movel.run(*action, speed = speed)

    #         signal.alarm(0)
    #     except TimeoutError as e:
    #         print("TimeOut")
    #     time.sleep(self.time_action)

    def run_move_linear_known(self, eef_list : list, speed=20, time_out=3):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(time_out)
        try:
            self.piper_arm.movel.run(*eef_list, speed = speed)
            signal.alarm(0)
        except TimeoutError as e:
            print("TimeOut")
        time.sleep(self.time_action)

    def run_move_curve(self, positions):
        self.piper_arm.movec.run(positions)
    
    def run_piper_movement(self, input_list : list, motion_speed=20, time_out=3):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(time_out)
        try:
            self.run_move_joint(input_list[:7], speed = motion_speed)
            self.run_move_linear_known(input_list[7:], speed = motion_speed, time_out = time_out)
            signal.alarm(0)
        except TimeoutError as e:
            print("TimeOut")

    def get_inverter(self, positions):
            inverted = [round(p / 1000) for p in positions]
            return inverted
    
    def get_joint_status(self):
        # print(self.get_inverter(self.piper_arm.check.get_joint_status()))
        return self.get_inverter(self.piper_arm.check.get_joint_status())

    def get_eef_status(self):
        # print(self.get_inverter(self.piper_arm.check.get_eef_status()))
        return self.get_inverter(self.piper_arm.check.get_eef_status())
    
    # def get_record_csv(self, filepath : str, joint_list : list, eef_list : list):
    #     '''
    #     This function captures stream of values and saves to CSV newline.

    #     Input : str, str
    #     Output : None
    #     '''
    #     with open(filepath, mode = 'a', newline = '') as csvfile:
    #         value_writer = csv.writer(csvfile, lineterminator = '\n')

    #         value_writer.writerow([*joint_list, *eef_list])
    #         csvfile.close()

    #     time.sleep(self.time_action * 10)
    
    # def run_record_csv(self, filepath : str):
    #     '''
    #     This function run PiPER accordingly to CSV file.

    #     Input : None
    #     Output : None
    #     '''
    #     restored_value = [0, 0, 0, 0, 0, 0, 0]
    #     row_count = 0

    #     with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
    #         value_reader = csv.reader(csvfile, lineterminator = '\n')
    #         for row_data in value_reader:
    #             processed_data = str(row_data).replace("'", "").replace("[", "").replace("]", "").split(",")
    #             restored_value = [int(x) for x in processed_data]
                
    #             # print(restored_value)
    #             self.run_piper_movement(restored_value)
    #             row_count = row_count + 1
    #             print(row_count)

def main():
    piper_left = PiPERControllerMK2(C_PiperInterface("piper_left"))
    # piper_left = PiPERControllerMK2(C_PiperInterface("piper_right"))

    print([*piper_left.get_joint_status(), *piper_left.get_eef_status()])

if __name__ == "__main__":
    main()

