
import os
from datetime import datetime
from collections import defaultdict

def generate_sales_report(txns,enriched,output="output/sales_report.txt"):
    os.makedirs(os.path.dirname(output), exist_ok=True)

    total=sum(t["Quantity"]*t["UnitPrice"] for t in txns)
    regions=defaultdict(float)

    for t in txns:
        regions[t["Region"]]+=t["Quantity"]*t["UnitPrice"]

    with open(output,"w",encoding="utf-8") as f:
        f.write("SALES ANALYTICS REPORT\n")
        f.write("="*40+"\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write(f"Total Revenue: INR {total:,.2f}\n\n")
        f.write("REGION SALES\n")
        for r,v in regions.items():
            f.write(f"{r}: INR {v:,.2f}\n")
