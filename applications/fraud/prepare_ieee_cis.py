"""Prepare a compact staged-evidence table from local IEEE-CIS CSV files.

No raw competition data is redistributed.
Standard-library implementation: suitable for streaming the large transaction file.
"""

from __future__ import annotations
import argparse, csv
from pathlib import Path

CORE = [
    "TransactionID","isFraud","TransactionDT","TransactionAmt","ProductCD",
    "card1","card2","card3","card4","card5","card6","addr1","addr2",
    "P_emaildomain","R_emaildomain"
]
CONTEXT_PREFIXES = ("C","D","M")
IDENTITY = ["TransactionID","DeviceType","DeviceInfo"] + [f"id_{i:02d}" for i in range(12,39)]

def load_identity(path: Path):
    rows={}
    with path.open(newline="",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        keep=[c for c in IDENTITY if c in (reader.fieldnames or [])]
        for row in reader:
            rows[row["TransactionID"]]={c:row.get(c,"") for c in keep if c!="TransactionID"}
    return rows

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--transaction",required=True)
    p.add_argument("--identity",required=True)
    p.add_argument("--out",default="artifacts/ieee_cis_staged.csv")
    p.add_argument("--limit",type=int,default=0)
    args=p.parse_args()

    identity=load_identity(Path(args.identity))
    out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)

    with Path(args.transaction).open(newline="",encoding="utf-8") as src:
        reader=csv.DictReader(src)
        context=[
            c for c in (reader.fieldnames or [])
            if len(c)>1 and c[0] in CONTEXT_PREFIXES and c[1:].isdigit()
        ]
        core=[c for c in CORE if c in (reader.fieldnames or [])]
        identity_cols=[c for c in IDENTITY if c!="TransactionID"]
        fields=core+context+identity_cols+["identity_available"]
        with out.open("w",newline="",encoding="utf-8") as dst:
            writer=csv.DictWriter(dst,fieldnames=fields)
            writer.writeheader()
            for i,row in enumerate(reader):
                if args.limit and i>=args.limit: break
                tid=row["TransactionID"]
                result={c:row.get(c,"") for c in core+context}
                idrow=identity.get(tid,{})
                result.update({c:idrow.get(c,"") for c in identity_cols})
                result["identity_available"]="1" if tid in identity else "0"
                writer.writerow(result)

    print(out)

if __name__=="__main__":
    main()
