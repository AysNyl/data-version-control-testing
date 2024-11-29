import glob
import pandas as pd


def comb_csv(path: str = ".", dest: str = ".") -> None:
    """Combine multiple csv files to single csv"""

    csv_iter = glob.glob("{}/*.csv".format(path))
    list_frame = list()

    dfs = pd.DataFrame()

    for csv_file in csv_iter:
        df = pd.read_csv(csv_file)
        df.columns = df.columns.str.strip()
        df = df.apply(lambda x: x.str.strip() if x.dtype == object else x).copy()
        df["DATE1"] = pd.to_datetime(df["DATE1"]).copy()
        df = df.set_index("DATE1").copy()
        list_frame.append(df)
        print(csv_file)

    dfs = pd.concat(list_frame)
    dfs.sort_index().to_csv("{}/sec_bhavdata_full_2024.csv".format(dest))
