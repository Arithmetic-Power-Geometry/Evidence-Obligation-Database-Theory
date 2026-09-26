"""Chronological progressive-information benchmark for creditcard.csv.

Requires pandas and scikit-learn. Thresholds are selected on validation only.
"""
import argparse, json
from pathlib import Path
import numpy as np, pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (average_precision_score,roc_auc_score,
 precision_recall_curve,precision_score,recall_score,f1_score,confusion_matrix)

p=argparse.ArgumentParser(); p.add_argument("csv"); p.add_argument("--out",default="artifacts/creditcard")
a=p.parse_args()
df=pd.read_csv(a.csv).sort_values("Time").reset_index(drop=True)
n=len(df); i1=int(.6*n); i2=int(.8*n)
tr,va,te=df.iloc[:i1],df.iloc[i1:i2],df.iloc[i2:]
stages={
"B0":["Time","Amount"],
"B1":["Time","Amount"]+[f"V{i}" for i in range(1,8)],
"B2":["Time","Amount"]+[f"V{i}" for i in range(1,15)],
"B3":["Time","Amount"]+[f"V{i}" for i in range(1,22)],
"B4":["Time","Amount"]+[f"V{i}" for i in range(1,29)]}
rows=[]; probs={}; decisions={}
for s,cols in stages.items():
    m=make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000,class_weight="balanced",solver="liblinear",random_state=0))
    m.fit(tr[cols],tr.Class)
    pv=m.predict_proba(va[cols])[:,1]; pt=m.predict_proba(te[cols])[:,1]
    pr,re,th=precision_recall_curve(va.Class,pv)
    f=2*pr[:-1]*re[:-1]/np.maximum(pr[:-1]+re[:-1],1e-15)
    t=float(th[int(np.nanargmax(f))]); pred=pt>=t
    tn,fp,fn,tp=confusion_matrix(te.Class,pred).ravel()
    rows.append(dict(stage=s,n_features=len(cols),threshold=t,pr_auc=average_precision_score(te.Class,pt),
      roc_auc=roc_auc_score(te.Class,pt),precision=precision_score(te.Class,pred,zero_division=0),
      recall=recall_score(te.Class,pred),f1=f1_score(te.Class,pred),tn=int(tn),fp=int(fp),fn=int(fn),tp=int(tp)))
    probs[s]=pt; decisions[s]=pred
out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
pd.DataFrame(rows).to_csv(out/"stage_metrics.csv",index=False)
rev=[]
for x,y in zip(list(stages)[:-1],list(stages)[1:]):
    ch=decisions[x]!=decisions[y]
    rev.append(dict(from_stage=x,to_stage=y,changed=int(ch.sum()),rate=float(ch.mean())))
pd.DataFrame(rev).to_csv(out/"decision_reversals.csv",index=False)
final=decisions["B4"]; hc=[]
for s in list(stages)[:-1]:
    mask=(probs[s]<=.01)|(probs[s]>=.99); d=decisions[s]!=final
    hc.append(dict(stage=s,high_conf_n=int(mask.sum()),high_conf_rate=float(mask.mean()),
      later_reversed_n=int((mask&d).sum()),later_reversed_rate=float((mask&d).sum()/max(mask.sum(),1))))
pd.DataFrame(hc).to_csv(out/"high_confidence_reversals.csv",index=False)
print(pd.DataFrame(rows).to_string(index=False))
