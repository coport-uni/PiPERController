import sys
import time
from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi import telemetrix_uno_r4_wifi
import logging

class PyArduino():
    def __init__(self):
        self.board = telemetrix_uno_r4_wifi.TelemetrixUnoR4WiFi(transport_type=1)

    def run_digital_write(self, pin_number : int, pin_state : bool):
        self.board.set_pin_mode_digital_output(pin_number)

        if pin_state is True:
            self.board.digital_write(pin_number, 0)
            logging.info(f'{pin_number} is {pin_state}')

        elif pin_state is False:
            self.board.digital_write(pin_number, 1)
            logging.info(f'{pin_number} is {pin_state}')
            

        time.sleep(0.001)

        # self.board.shutdown()
    
    def get_digital_state(self, pin_number : int):
        global digital_value
        digital_value = None
        self.board.set_pin_mode_digital_input_pullup(pin_number, callback = self.get_digital_state_slicer)
        
        while digital_value is None:
            time.sleep(0.01)

        # self.board.shutdown()

        return digital_value

    def get_digital_state_slicer(self, data):
        global digital_value
        pin_mode_index = 0
        pin_number_index = 1
        pin_state_index = 2

        digital_value = data[pin_state_index]

    def get_analog_state(self, pin_number : int):
        global analog_value
        analog_value = None
        self.board.set_pin_mode_analog_input(pin_number, differential = 0, callback = self.get_analog_state_slicer)

        while analog_value is None:
            time.sleep(0.01)

        # self.board.shutdown()

        return analog_value

    def get_analog_state_slicer(self, data):
        global analog_value
        pin_mode_index = 0
        pin_number_index = 1
        pin_state_index = 2

        # print(data[pin_state_index])

        analog_value = data[pin_state_index]
    
def main():
    pa = PyArduino()
    # 센서 예제
    while True:
        value0 = pa.get_analog_state(0)
        print("A0 is " + str(value0))
        value1 = pa.get_analog_state(1)
        print("A1 is " + str(value1))
    # while True:
    #     value = pa.get_digital_state(8)
    #     print(value)
    
    # 디지털 입출력 예제
    # for pin_number in range(4,8):
    #     pa.run_digital_write(pin_number, True)
    #     time.sleep(1)
    #     pa.run_digital_write(pin_number, False)

    # 밸브, 외란 펌프 예제
    # pa.run_digital_write(4, True)
    # pa.run_digital_write(5, True)
    
    # pa.run_digital_write(6, True)
    # pa.run_digital_write(7, True)


if __name__ == '__main__':
    main()