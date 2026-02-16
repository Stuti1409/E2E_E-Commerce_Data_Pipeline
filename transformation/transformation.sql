CREATE OR REPLACE TABLE sales_summary AS
SELECT product, SUM(amount) AS total_sales, COUNT(order_id) AS total_orders
FROM fact_orders
GROUP BY product;