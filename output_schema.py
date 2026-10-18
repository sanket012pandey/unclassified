from pydantic import BaseModel
from typing import Literal

class OutputSchema(BaseModel):
    prediction_classifier: Literal['ham' ,'spam']   