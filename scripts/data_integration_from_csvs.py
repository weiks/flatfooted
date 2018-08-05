
import os
import tqdm
import pandas as pd

from pandas.errors import EmptyDataError

data_dir = "/media/otrenav/Second/Projects/mike-weiksner/flatfooted/outputs"
full = None

for f in tqdm.tqdm(os.listdir(data_dir)):
    if "csv" in f:
        try:
            data = pd.read_csv("{}/{}".format(data_dir, f))
        except EmptyDataError as e:
            pass
        else:
            if not data.empty and full is None:
                full = data
            elif not data.empty:
                full = pd.merge(full, data, how="outer")

print("-" * 100)
print(full.shape)
print("-" * 100)

full.to_csv("data_csvs.csv", index=False)
