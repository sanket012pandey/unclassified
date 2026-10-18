from fastapi import FastAPI
from input_schema import inputSchema
from output_schema import OutputSchema
from predict import make_prediction

app = FastAPI()


@app.post('/predict' , response_model= OutputSchema)
def  prediction(user_input:inputSchema):
   result = make_prediction(user_input.model_dump())
   return OutputSchema(prediction_classifier = result)