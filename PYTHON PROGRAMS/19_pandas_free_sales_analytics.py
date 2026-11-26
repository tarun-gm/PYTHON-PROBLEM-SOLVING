import argparse
import csv
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


def sales_summary(path):
    revenue_by_product = defaultdict(Decimal)
    units_by_product = defaultdict(int)
    revenue_by_month = defaultdict(Decimal)
    with Path(path).open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        required = {"date", "product", "quantity", "unit_price"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"CSV must contain columns: {sorted(required)}")
        for row in reader:
            quantity = int(row["quantity"])
            unit_price = Decimal(row["unit_price"])
            revenue = quantity * unit_price
            product = row["product"].strip()
            month = row["date"][:7]
            revenue_by_product[product] += revenue
            units_by_product[product] += quantity
            revenue_by_month[month] += revenue
    ranking = sorted(revenue_by_product.items(), key=lambda item: item[1], reverse=True)
    return ranking, dict(revenue_by_month), dict(units_by_product)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    ranking, monthly, units = sales_summary(args.file)
    print("Product revenue")
    for product, revenue in ranking:
        print(product, revenue, units[product])
    print("Monthly revenue")
    for month, revenue in sorted(monthly.items()):
        print(month, revenue)


if __name__ == "__main__":
    main()
