from pydantic import BaseModel


class BenfordResponse(BaseModel):
    P: float
    t: float
    prediction: bool
    percentage_matrix: list[list[float]]