# PiPER 개발
## Setup
* 교안자료 기반으로 작업
* conda보다는 venv가 좋을 듯
```bash
# python 3.8 버전 활용할 것! 
# => 그럼 Conda가 좋을까? But ROS와 궁합이.. => 절충: venv 활용

# 환경 설정
sudo apt install python3.8-venv
python3-m venv piper
source piper/bin/activate

# 의존성 설치
pip3 install python-can piper_sdk
sudo apt update && sudo apt install iproute2 can-utils ethtool
git clone https://github.com/agilexrobotics/piper_sdk.git

# CAN, USB 포트 / 탐색
cd piper_sdk
bash find_all_can_port.sh
bash can_activate.sh can0 1000000
sudo ethtool -i can0 | grep bus

# CAN 포트 이름 지정
# 후에 
bash can_activate.sh piper_left 1000000 "3-1:1.0"

# 연결확인
candump piper_left
```
* 관절 구동정도
	* 최대값에서 +-5씩하면 안전할 듯?
		* 그리퍼 0 ~ 65
		* 1번 -149 ~ 149
		* 2번 3 ~ 177
		* 3번 0 ~ 160
		* 4번 -95 ~ 95 
		* 5번 -70 ~ 70
		* 6번 -115 ~ 115
	* ![[Pasted image 20250709203416.png]]
## Code
```python title:main.py
from typing import (
    Optional,
)
from piper_sdk import *
import time

class PiperController():
    def __init__(self):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        self.piper_left = C_PiperInterface_V2("piper_left")
        self.piper_left.ConnectPort()

        while not self.piper_left.EnablePiper():
            time.sleep(0.01)    

        self.time_delay = 1
        self.motion_factor = 1000

    def get_position_joint(self):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        message = str(self.piper_left.GetArmJointMsgs())
        time.sleep(self.time_delay)

        joint_index = [0, 0, 0, 0, 0, 0, 0]
        joint_state = [0, 0, 0, 0, 0, 0, 0]
        
        for index_number in range(6):
            joint_index[index_number] = message.find(f"Joint {index_number + 1}:")

        for joint_number in range(6):
            joint_state[joint_number] = round(float(message[joint_index[joint_number] + 8:joint_index[joint_number + 1] - 1]) / self.motion_factor)

        joint_state[6] = self.get_position_gripper()

        return joint_state

    def get_position_gripper(self):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        message = str(self.piper_left.GetArmGripperMsgs())

        gripper_index_string = ["grippers_angle: ", ","]

        gripper_index_number = [0,0]

        for index_number in range(2):
            gripper_index_number[index_number] = message.find(gripper_index_string[index_number])

        gripper_state = int(message[gripper_index_number[0] + 16:gripper_index_number[1]]) / self.motion_factor

        return gripper_state

    def get_position_eef(self):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        message = str(self.piper_left.GetArmEndPoseMsgs())
        eef_index_string = ["X_axis : ", "Y_axis : ", "Z_axis : ", "RX_axis : ", "RY_axis : ", "RZ_axis : "]

        eef_index = [0, 0, 0, 0, 0, 0, 0]
        eef_state = [0, 0, 0, 0, 0, 0, 0]

        for index_number in range(6):
            eef_index[index_number] = message.find(eef_index_string[index_number])
        
        for eef_number in range(6):
            eef_state[eef_number] = int(message[eef_index[eef_number] + 9:eef_index[eef_number + 1] - 1]) / self.motion_factor

        eef_state[6] = self.get_position_gripper()

        return eef_state

    def get_normalized_value(self, value_max, value_min, value_input):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        if value_min <= value_input <= value_max:

            return value_input * self.motion_factor
        
        elif value_min > value_input:

            return value_min * self.motion_factor
        
        elif value_input > value_max:

            return value_max * self.motion_factor

    def run_position_gripper(self, gripper_mm):
        '''
        This function captures live mouse position.

        Input : None
        Output : dict
        '''
        gripper_mm = self.get_normalized_value(68, -2, gripper_mm)
        self.piper_left.GripperCtrl(0,1000,0x02, 0)
        print(gripper_mm)
        self.piper_left.GripperCtrl(gripper_mm, 1000, 0x01, 0)
        time.sleep(0.005)

        return True

def main():
    '''
    This function captures live mouse position.

    Input : None
    Output : dict
    '''
    pc = PiperController()
    while True:
        pc.run_position_gripper(68)
        time.sleep(3)
        pc.run_position_gripper(0)
        time.sleep(3)

    # while True:
    #     print(pc.get_position_eef())

    # while True:
    #     print(pc.get_position_joint())
    
if __name__ == "__main__":
    main()
```
## Result
