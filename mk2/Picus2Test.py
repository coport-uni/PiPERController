import serial
import time

class Picus2Controller:
    def __init__(self, port : str):
        self.serial = serial.Serial(port, 9600, timeout=1)

    def run_serial_command(self, command_type: str, command_data : str, delay = 0.5):
        try:
            finalize_command = "{" + "\"" + command_type + "\"" + ":" + "\"" + command_data + "\"" + "}"+ "\r\n"
            # print(finalize_command)
            finalize_command = finalize_command.encode()
            self.serial.write(finalize_command)
            time.sleep(delay)
        
            if self.serial.in_waiting > 0:
                response = self.serial.readline().decode('utf-8').strip()
                # print(response)

        except:
            print("comm_error")

    
    def run_scenario(self):
        # Getting in menu
        self.run_serial_command("button", "TRIGGER_BUTTON_POWER")
 
        for i in range(4):
            self.run_serial_command("button", "DOWN")
 
        self.run_serial_command("button", "TRIGGER_BUTTON_TOP")

        # Start 9 dispensing mode - charge liquid
        self.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        time.sleep(3)
        self.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        
        print("Prep Complete")
        time.sleep(3)

        # Dispense remained liquid
        for i in range(9):
            self.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        
        print("Dispense Complete")

        # Trashing remained liquid
        self.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        for i in range(3):
            self.run_serial_command("button", "TRIGGER_BUTTON_TOP_DOUBLE", delay=0.25)

if __name__ == "__main__":
    p2c = Picus2Controller("/dev/ttyACM2")
    p2c.run_scenario()