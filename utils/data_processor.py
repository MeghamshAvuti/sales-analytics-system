
import os

def parse_transactions(lines):
    txns=[]
    for l in lines:
        try:
            t,d,pid,pname,q,price,cid,r = l.split("|")
            txns.append({
                "TransactionID":t,
                "Date":d,
                "ProductID":pid,
                "ProductName":pname,
                "Quantity":int(q),
                "UnitPrice":float(price),
                "CustomerID":cid,
                "Region":r
            })
        except:
            continue
    return txns

def validate_transactions(txns):
    valid=[]
    invalid=0
    for t in txns:
        if t["Quantity"]>0 and t["UnitPrice"]>0:
            valid.append(t)
        else:
            invalid+=1
    return valid, invalid

def enrich_sales_data(txns, mapping):
    enriched=[]
    for t in txns:
        e=t.copy()
        pid=int(e["ProductID"][1:])
        api=mapping.get(pid)
        if api:
            e.update(api)
            e["API_Match"]=True
        else:
            e.update({"API_Category":None,"API_Brand":None,"API_Rating":None})
            e["API_Match"]=False
        enriched.append(e)
    return enriched

def save_enriched_data(data, filename="data/enriched_sales_data.txt"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename,"w",encoding="utf-8") as f:
        headers=data[0].keys()
        f.write("|".join(headers)+"\n")
        for d in data:
            f.write("|".join(str(d[h]) for h in headers)+"\n")
