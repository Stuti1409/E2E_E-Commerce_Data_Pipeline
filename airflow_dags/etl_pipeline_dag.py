from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime

default_args = {"start_date": datetime(2024, 1, 1)}

with DAG("snowflake_pipeline", schedule_interval = "@hourly", default_args = default_args, catchup = False) as dag:
    transform =  SnowflakeOperator(
        task_id = "run_transformations",
        sql = "transformation/transformation.sql",
        snowflake_conn_id = "snowflake_default"
    )