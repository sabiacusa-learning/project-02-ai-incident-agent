
import pandas as pd

def search_logs(keyword):
    df = pd.read_csv("data/logs.csv")
    return df[df["message"].str.contains(keyword, case=False)].to_dict()