
import pandas as pd

id_columns = ["search_string", "site_name", "timestamp"]
data_csvs = pd.read_csv("./data_csvs.csv")
data_jsons = pd.read_csv("./data_jsons.csv")

full = pd.merge(data_csvs, data_jsons, how="outer")
full.drop_duplicates(inplace=True)

print("-" * 100)
print(full.shape)
print("-" * 100)

full.to_csv("data.csv", index=False)
