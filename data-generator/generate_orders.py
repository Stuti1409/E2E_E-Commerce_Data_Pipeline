import pandas as pd
import random
from datetime import datetime, timedelta

products = ["Phone", "Laptop", "Headphones", "Watch", "Shoes"]
cities = ["Mumbai", "Delhi", "Chennai", "Banglore"]

data = []

for i in range(1000):
    data.append({
        "order_id": i,
        "customer_id": random.randint(1, 200),
        "product": random.choice(products),
        "amount": random.randint(500, 50000),
        "city": random.choice(cities),
        "order_time": datetime.now() - timedelta(minutes=random.randint(1, 10000))
    })

    df = pd.DataFrame(data)
    df.to_csv("orders.csv", index=False)
    print("Orders file created")