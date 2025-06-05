import pandas as pd
import numpy as np  

names = ["equity_capital", "reserves", "borrowings", "other_liabilities", "total_liabilitites", "fixed_assets", "cwip", "investments", "other_assets", "total_assets", "ticker"]
df = pd.read_csv("balance_sheet.csv", names=names)

period = []
for i in df.index:
    period.append(pd.to_datetime(i))

print(type(period[0]))

