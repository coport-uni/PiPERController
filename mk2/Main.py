import LOHCAction1
from PyArduino import PyArduino
import time

def main():
    pa = PyArduino()
    print("init")

    # Test Relay with robotic action
    pa.run_digital_write(2, True)
    time.sleep(1)
    # pa.run_digital_write(2, False)
    # time.sleep(1)
    # pa.run_digital_write(3, True)
    # time.sleep(1)
    # pa.run_digital_write(3, False)
    # time.sleep(1)

    # LOHCAction1.run_lohc_action_1()

main()