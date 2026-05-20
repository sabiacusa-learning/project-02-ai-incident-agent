
import pandas as pd

def get_deployments(service):
    df = pd.read_csv("data/deployments.csv")
    return df[df["service"] == service].to_dict()