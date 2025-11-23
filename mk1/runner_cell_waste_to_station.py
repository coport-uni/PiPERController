from piper_contorller import PiperController
from tqdm import tqdm

def main():
    '''
    This function moves PiPER with CSV files.

    Input : None
    Output : None
    '''
    pc = PiperController()
    csv_filepath = "action_csv/cell_waste_to_station/cell_waste_to_station"

    for i in tqdm(range(1), desc="Moving object as designated"):
        pc.run_initialization()
        pc.run_record_csv(csv_filepath + "aa.csv")
        pc.run_motion_compensation()
        pc.run_record_csv(csv_filepath + "ab.csv")
        pc.run_motion_compensation()
        pc.run_record_csv(csv_filepath + "ac.csv")
        pc.run_motion_compensation()
        pc.run_record_csv(csv_filepath + "ad.csv")
        pc.run_motion_compensation()
        pc.run_record_csv(csv_filepath + "ae.csv")
        pc.run_motion_compensation()

if __name__ == "__main__":
    main()