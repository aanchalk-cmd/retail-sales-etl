import pandas as pd
# Load datasets
customers = pd.read_csv("data/raw/customers.csv")
products = pd.read_csv("data/raw/products.csv")
sales = pd.read_csv("data/raw/sales.csv")
inventory = pd.read_csv("data/raw/inventory.csv")

# 1. Check invalid customer references
invalid_customers = sales[
    ~sales["customer_id"].isin(customers["customer_id"])
]

# 2. Check invalid product references in sales
invalid_sales_products = sales[
    ~sales["product_id"].isin(products["product_id"])
]

# 3. Check invalid product references in inventory
invalid_inventory_products = inventory[
    ~inventory["product_id"].isin(products["product_id"])
]

# 4. Check invalid store IDs
valid_stores = ["S001", "S002", "S003", "S004", "S005"]

invalid_sales_stores = sales[
    ~sales["store_id"].isin(valid_stores)
]

invalid_inventory_stores = inventory[
    ~inventory["store_id"].isin(valid_stores)
]

# Display results
print("Invalid customer references:", len(invalid_customers))
print("Invalid sales product references:", len(invalid_sales_products))
print("Invalid inventory product references:", len(invalid_inventory_products))
print("Invalid sales store references:", len(invalid_sales_stores))
print("Invalid inventory store references:", len(invalid_inventory_stores))

# Display sample invalid records
print("\nInvalid customer sample:")
print(invalid_customers.head().to_string(index=False))

print("\nInvalid product sample:")
print(invalid_sales_products.head().to_string(index=False))
