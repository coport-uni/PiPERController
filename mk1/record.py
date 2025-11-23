from piper_contorller import PiperController

def main():
    '''
    This function captures PiPER joint space data stream.

    Input : None
    Output : None
    '''
    pc = PiperController()
    # csv_filepath = "action_csv/vial_shake/vial_shake.csv"
    # csv_filepath = "action_csv/open_spectro/open_spectro.csv"
    # csv_filepath = "action_csv/close_spectro/close_spectro.csv"
    # csv_filepath = "action_csv/cell_to_scale/cell_to_scale.csv"
    # csv_filepath = "action_csv/vial_waste_to_station/vial_waste_to_station.csv"
    # csv_filepath = "action_csv/cell_waste_to_station/cell_waste_to_station.csv"
    csv_filepath =  "action_csv/cell_to_spectro/cell_to_spectro.csv"


    while True:
        data = pc.get_position_joint()
        pc.get_record_csv(csv_filepath, data)
        print(data)

if __name__ == "__main__":
    main()
    # split action_csv/vial_shake/vial_shake.csv -l 100 vial_shake
    # rename 's/$/.csv/' *