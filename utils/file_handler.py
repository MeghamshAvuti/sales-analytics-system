
def read_sales_data(filename):
    encodings = ["utf-8","latin-1","cp1252"]
    for enc in encodings:
        try:
            with open(filename,"r",encoding=enc) as f:
                return [l.strip() for l in f.readlines()[1:] if l.strip()]
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print("✗ sales_data.txt not found")
            return []
    return []
