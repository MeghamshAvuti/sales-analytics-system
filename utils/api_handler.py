
import requests

def fetch_all_products():
    try:
        r=requests.get("https://dummyjson.com/products?limit=100",timeout=10)
        r.raise_for_status()
        return r.json().get("products",[])
    except Exception as e:
        print("✗ API Error:",e)
        return []

def create_product_mapping(products):
    mapping={}
    for p in products:
        mapping[p.get("id")] = {
            "API_Category":p.get("category"),
            "API_Brand":p.get("brand"),
            "API_Rating":p.get("rating")
        }
    return mapping
