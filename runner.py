from piper_contorller import PiperController
from tqdm import tqdm

def main():
    '''
    This function captures live mouse position.

    Input : None
    Output : dict
    '''
    pc = PiperController()
    csv_filepath_down = "action_csv/test_demo_down.csv"
    csv_filepath_up = "action_csv/test_demo_up.csv"

    for i in tqdm(range(2), desc="Moving object as designated"):
        pc.run_initialization()
        pc.run_record_csv(csv_filepath_up)
        pc.run_initialization()
        pc.run_record_csv(csv_filepath_down)

if __name__ == "__main__":
    main()