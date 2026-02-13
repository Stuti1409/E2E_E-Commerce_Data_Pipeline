CREATE OR REPLACE PIPE orders_pipe
AUTO_INGEST = TRUE
AS
COPY INTO raw_orders
FROM @s3_stage
FIKE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1);

CREATE OR REPLACE TABLE dim_product AS SELECT DISTINCT product FROM raw_orders;

CREATE OR REPLACE TABLE dim_customer AS SELECT DISTINCT customer_id, city FROM raw_orders;

CREATE OR REPLACE TABLE fact_orders AS SELECT order_id, customer_id, product,amount, order_time FROM raw_orders;