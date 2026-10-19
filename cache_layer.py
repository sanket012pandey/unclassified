import redis
import hashlib
import json
from typing import List
from pydantic import BaseModel
from input_schema import inputSchema
from output_schema import OutputSchema
from predict import make_prediction
import joblib

saved_model = joblib.load("spam_model.joblib")

redis_client  = redis.Redis( host = 'localhost', port = 6379 , db= 0 )

def cache_key( input:inputSchema) -> str:
    raw = json.dumps(input.model_dump() , sort_keys=True)
    return f"predict :{hashlib.sha256(raw.encode()).hexdigest()}"

def get_cached_prediction(input:inputSchema):
    key = cache_key(input)
    cached_result = redis_client.get(key)
    if cached_result:
        print('success fetched from cache')
        return OutputSchema(**json.loads(cached_result))
    return None

def  save_new_pred(input:inputSchema):
    key = cache_key(input)
    result = make_prediction(input.model_dump())
    response_data =  OutputSchema(prediction_classifier = result)
    redis_client.set(key , response_data.model_dump_json() , ex = 3600)

    return response_data
