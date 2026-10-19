from fastapi import FastAPI
from input_schema import inputSchema
from output_schema import OutputSchema
from predict import make_prediction
from cache_layer import  get_cached_prediction , save_new_pred , cache_key
import json

app = FastAPI()


@app.post('/predict' , response_model= OutputSchema)
async def  prediction(user_input:inputSchema):
   key = cache_key(input.input)

   cached_result = get_cached_prediction(user_input)
   
   #checking in cache
   if cached_result:
      print('successfully fetched results from cache')
      return json.loads(cached_result)
   
   result = make_prediction(input.model_dump())
   response_data =  OutputSchema(prediction_classifier = result)
   from fastapi import FastAPI
from input_schema import inputSchema
from output_schema import OutputSchema
from predict import make_prediction
from cache_layer import  get_cached_prediction , save_new_pred , cache_key
import json

app = FastAPI()


@app.post('/predict' , response_model= OutputSchema)
async def  prediction(user_input:inputSchema):

   cached_result = get_cached_prediction(user_input)
   #checking in cache
   if cached_result:
      print('successfully fetched results from cache')
      return cached_result

   #if not
   response_data =  save_new_pred(user_input)
   return response_data

