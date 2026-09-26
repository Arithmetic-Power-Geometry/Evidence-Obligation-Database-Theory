import argparse, pandas as pd

p=argparse.ArgumentParser()
p.add_argument("csv")
args=p.parse_args()

df=pd.read_csv(args.csv).sort_values("Time").reset_index(drop=True)
assert set(["Time","Amount","Class"]+[f"V{i}" for i in range(1,29)]).issubset(df.columns)

print("rows",len(df))
print("columns",len(df.columns))
print("missing",int(df.isna().sum().sum()))
print("fraud",int(df.Class.sum()))
print("fraud_rate",float(df.Class.mean()))

n=len(df)
for name,a,b in [("train",0,.6),("validation",.6,.8),("test",.8,1)]:
    x=df.iloc[int(a*n):int(b*n)]
    print(name,len(x),int(x.Class.sum()),float(x.Class.mean()))
