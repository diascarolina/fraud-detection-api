import os
import uvicorn
import pickle
import logging
import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

app = FastAPI()

model_path = os.path.join(os.path.dirname(__file__), 'modelo/modelo.pkl')
model = pickle.load(open(model_path, 'rb'))


@app.get('/health', status_code=200)
def health_check():
    return JSONResponse({"status": "Up and running"})


@app.post('/predict')
async def predict(request: Request):
    try:
        json_data = await request.json()
        data = pd.DataFrame(json_data, index=[0])
        preds = model.predict(data)[0]
        return JSONResponse({"status": "success", "predicted_class": f"{preds}"})
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Prediction failed.")


@app.post("/predict_batch")
async def predict_batch(request: Request):
    """
    Expects a json array.
    """
    try:
        json_data = await request.json()
        df = pd.DataFrame(json_data)
        df["preds"] = model.predict(df)
        return JSONResponse({"status": "success", "predictions": f"{df['preds'].to_json(orient='records')}"})
        
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Batch prediction failed.")


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=os.environ.get('PORT', 8000))
