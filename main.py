
from utils.file_handler import read_sales_data
from utils.data_processor import *
from utils.api_handler import *
from utils.report_generator import generate_sales_report

def main():
    print("="*40)
    print("SALES ANALYTICS SYSTEM")
    print("="*40)

    raw = read_sales_data("data/sales_data.txt")
    print(f"✓ Successfully read {len(raw)} transactions")

    parsed = parse_transactions(raw)
    valid, invalid = validate_transactions(parsed)
    print(f"✓ Valid: {len(valid)} | Invalid: {invalid}")

    products = fetch_all_products()
    mapping = create_product_mapping(products)

    enriched = enrich_sales_data(valid, mapping)
    save_enriched_data(enriched)

    generate_sales_report(valid, enriched)
    print("✓ Process Complete")

if __name__ == "__main__":
    main()
