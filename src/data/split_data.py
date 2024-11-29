import pathlib
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

curr_path = pathlib.Path(__file__)

home_dir = curr_path.parent.parent.parent

def save_data(train, test):
    out_path = home_dir.as_posix() + "/data/interim"
    pathlib.Path(out_path).mkdir(parents=True, exist_ok=True)
    train.to_csv(out_path + "/train.csv")
    test.to_csv(out_path + "/test.csv")

def main():
    df = pd.read_csv(home_dir.as_posix() + "/data/raw/sec_bhavdata_full_2024.csv", index_col="DATE1")
    print(df)
    save_data(*train_test_split(df, random_state=42))
    
    
if __name__ == "__main__":
    main()

