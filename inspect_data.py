import pandas as pd
import os

data_path = "data/raw"

for file in os.listdir(data_path):
    if file.endswith(".csv"):
        file_path = os.path.join(data_path, file)

        df = pd.read_csv(file_path)

        print("\n================================")
        print(f"FILE NAME: {file}")
        print("================================")

        print("Shape:", df.shape)
        print("Columns:", df.columns.tolist())

        print("\nData TYpes:")
        print(df.dtypes)

        print("\nFirst 5 Records:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

customers = pd.read_csv("data/raw/customers.csv")
products = pd.read_csv("data/raw/products.csv")
sales = pd.read_csv("data/raw/sales.csv")
inventory = pd.read_csv("data/raw/inventory.csv")

print("\ncustomers")
print("Unique:", customers["customer_id"].is_unique)

print("\nPRODUCTS")
print("Unique:", products["product_id"].is_unique)

print("\nSALES")
print("Unique:", sales["transaction_id"].is_unique)
print("Duplicate IDs:", sales["transaction_id"].duplicated().sum())

print("\nINVENTORY")
print(
    "Duplicate combinations:",
    inventory.duplicated(
        subset=["product_id", "store_id"]
    ).sum()
)