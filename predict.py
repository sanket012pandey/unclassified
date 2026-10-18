import joblib

saved_model = joblib.load("spam_model.joblib")
print("MODEL LOADED SUCCESS")
print(saved_model.named_steps.keys())

def make_prediction(data: dict) -> str:
    raw = saved_model.predict([data["Email"]])[0]
    return str(raw)