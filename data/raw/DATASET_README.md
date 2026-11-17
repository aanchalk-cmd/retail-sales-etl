# Retail Sales & Inventory ETL - Dataset Guide

## Files
- `customers.csv`: 1,000 customer master records.
- `products.csv`: 500 product master records with category and list price.
- `sales.csv`: 15,120 rows (15,000 generated transactions plus 120 exact duplicate rows).
- `inventory.csv`: 2,500 product/store inventory snapshot rows.

Total: 19,120 CSV data rows.

## Important columns
- `sales.unit_price` is the actual transaction price. Compare it with `products.unit_price` to flag invalid or suspicious prices.
- `sales.sale_timestamp` is a timestamp string; parse and validate it.
- `store_id` values should be one of S001-S005.
- `transaction_id` is the transaction's business key.
- `inventory` is a current stock snapshot by product and store, not a stock movement history.

## Intentionally injected data-quality issues
- Sales: missing customer IDs, unknown customer IDs, unknown product IDs, zero/negative quantities, zero/negative/extreme prices, malformed timestamps, invalid store IDs, and exact duplicate transaction rows.
- Inventory: negative stock, unknown product IDs, and malformed update timestamps.
- These defects are deliberate. Do not silently delete everything: define validation rules, retain rejected rows in a reject/quarantine table or file, and log rejection reasons.

## Suggested assumptions
- Treat `transaction_id` as unique.
- A valid sale must reference an existing customer and product, use a known store ID, have quantity > 0, have a parseable timestamp, and have a positive unit price.
- For suspicious prices, define a documented rule (for example, flag actual unit price above product list price or more than 30% below list price). Do not assume every discount is invalid.
- Inventory stock must be >= 0 and reference a known product and store.
- Use synthetic data only; all customer emails use the reserved `example.com` domain.

## Suggested project challenge
Build an idempotent ETL pipeline: running it twice should not duplicate accepted sales or inventory records. Use database constraints/upserts and an ETL run log.
