import numpy as np
from fastapi import FastAPI
from userdata import UserData
from respmodel import BenfordResponse
from benfordslaw import benfordslaw

app = FastAPI()


@app.post("/fraud_detector", response_model=BenfordResponse)
def fraud_detector(potential_fraudulent_dataset: UserData):
    # print(type(potential_fraudulent_dataset))
    np_data = np.array(potential_fraudulent_dataset.data)
    bl = benfordslaw(alpha=0.05, method="chi2", pos=1)
    results = bl.fit(np_data)
    return BenfordResponse(
        P=results["P"],
        t=results["t"],
        prediction=results["P_significant"],
        percentage_matrix=results["percentage_emp"].tolist(),
    )