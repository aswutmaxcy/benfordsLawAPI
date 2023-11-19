import requests
import pandas as pd
import numpy as np

filled_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    1,
    1,
    1,
    1,
    1,
    2,
    2,
    2,
    2,
    3,
    3,
    4,
    5,
    7,
    8,
    9,
]

fraudulent_list = np.random.randint(0, high=100, size=1000).tolist()

data = pd.read_csv("example_datasets/president_county.csv")
county_votes = data["total_votes"].tolist()


req_data = {"data": filled_list}

resp = requests.post("http://localhost:8000/fraud_detector", json=req_data)

print(resp.json())