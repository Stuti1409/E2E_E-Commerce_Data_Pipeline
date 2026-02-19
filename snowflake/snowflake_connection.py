import snowflake.connector

conn = snowflake.connector.connect(
    user = '',
    password = '',
    account = '', 
    warehouse = 'COMPUTE_WH',
    database = "ECOM_DB",
    schema = 'PUBLIC'
)

cur = conn.cursor()
cur.execute("SELECT CURRENT_VERSION()")
print(cur.fetchone())
cur.close()
conn.close()