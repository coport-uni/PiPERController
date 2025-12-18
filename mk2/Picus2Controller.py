import serial
import time

class Picus2Controller:
    def __init__(self, port : str):
        """
        This function get address of Picus2 from user and initialize serial communication.

        Input : String
        Output : None
        """
        self.serial = serial.Serial(port, 9600, timeout=1)

    def run_serial_command(self, command_type: str, command_data : str, delay = 0.5):
        """
        This function refactor user-friendly command to Picus2 format. READ Picus2 API document for more information. 

        Input : String, String, float
        Output : None
        """
        try:
            finalize_command = "{" + "\"" + command_type + "\"" + ":" + "\"" + command_data + "\"" + "}"+ "\r\n"
            finalize_command = finalize_command.encode()
            self.serial.write(finalize_command)
            time.sleep(delay)
        
            if self.serial.in_waiting > 0:
                response = self.serial.decode('utf-8').strip()
                # print(response)
        except:
            pass
            # print("comm_error")

    
    def run_scenario(self):
        """
        This function is simple scenario case for LOHC experimentation. Since MIT emphasize more user-friendly code, i use for loop.

        Input : None
        Output : None
        """
        # 1) Getting in menu
        self.run_serial_command("button", "TRIGGER_BUTTON_POWER")
 
        for i in range(4):
            self.run_serial_command("button", "DOWN")
 
        self.run_serial_command("button", "TRIGGER_BUTTON_TOP")

        # 2) Start 20 dispensing mode - charge liquid
        self.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        time.sleep(4)
        
        print("Prep Complete")

        # 3) Dispense remained liquid
        self.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        self.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        
        print("Dispense Complete")

        self.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        self.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        
        print("Dispense Complete")

        self.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        self.run_serial_command("button", "TRIGGER_BUTTON_TOP")
        
        print("Dispense Complete")

    def run_test(self):
        self.run_serial_command("data", "GET_VERSION")

if __name__ == "__main__":
    """
    This function holds example main flow

    Input : None
    Output : None
    """
    # sudo dmesg | grep tty
    p2c = Picus2Controller("/dev/ttyACM1")
    
    # sudo rfcomm bind 0 FE:BE:2D:A2:35:1F
    # p2c = Picus2Controller("/dev/rfcomm0")
    p2c.run_scenario()
    # p2c.run_test()