import pandas as pd
import json
def getStocks():
    df = pd.read_csv("Equity.csv", index_col=False)
    return df["Security Id"][1775:]

