# benfordsLawAPI
The purpose of this personal project is to use the bendfordslaw package (sorts given numbersets into a Benford's Law distribution visualized in a graph and text) to detect fraud in given datasets.

# Results
You'll receive the integers 1-9 and percentages given to each number, a true/false assessment and a numpy array to plot.

# Maintence
Anyone can contribute and I will check in weekly the next few months to review merge requests.

## TLDR
Docker Build & Run
```sh
docker build -t bendfordsLawAPI:local .
docker run --rm -it bendfordsLawAPI:local
```

## Python Startup
```sh
git clone https://github.com/aswutmaxcy/benfordsLawAPI.git
cd benfordsLawAPI
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Submitting a Dataset
```python
import requests

sample_list = [1, 1, 1, 2, 2, 3, 4]
req_data = {"data": sample_list}
resp = request.post("http://localhost:8000/fraud_detector", json=req_data)
print(resp.json())
```
## Read From a CSV File
[checkout this example](request.py#35)
