from piper_contorller import PiperController

def main():
    '''
    This function captures live mouse position.

    Input : None
    Output : dict
    '''
    pc = PiperController()
    # csv_filepath = "action_csv/test_demo.csv"
    csv_filepath = "action_csv/test_demo_down.csv"

    while True:
        data = pc.get_position_joint()
        pc.get_record_csv(csv_filepath, data)
        print(data)

if __name__ == "__main__":
    main()