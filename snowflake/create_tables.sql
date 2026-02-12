CREATE OR REPLACE TABLE raw_orders(
    order_id INT,
    customer_id INT,
    product STRING,
    amount INT,
    city STRING,
    order_time TIMESTAMP
);

CREATE OR REPLACE STAGE s3_stage
URL = 's3://bucket-name/'
CREDENTIALS = (AWS_KEY_ID = '' AWS_SECRET_KEY = '');