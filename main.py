import joblib
import io
import pandas as pd
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel,Field 
app = FastAPI()

# Load model and features when server starts
model = joblib.load("house_model.joblib")
features = joblib.load("house_features.joblib")

print("Model loaded successfully!")
class HouseFeatures(BaseModel):
    MedInc: float = Field(gt=0, description="Median income in block group")
    HouseAge: float = Field(gt=0, description="Median house age in block group")
    AveRooms: float = Field(gt=0, description="Average number of rooms per household")
    AveBedrms: float = Field(gt=0, description="Average number of bedrooms per household")
    Population: float = Field(gt=0, description="Block group population")
    AveOccup: float = Field(gt=0, description="Average house occupancy")
    Latitude: float = Field(ge=32,le=42, description="Block group latitude")
    Longitude: float = Field(ge=-125,le=-114 ,description="Block group longitude")

# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------
@app.get("/")
def home():
    return {
        "message": "California house price prediction api",
        "status": "running",
        "endpoint": "send POST request to /predict/"
    }

@app.get("/health")
def health():
    return{
        "status":"runnning",
        "model":"Randomforestregressor",
        "features":features,
        "avg_error":"$39,000"
    }
@app.post("/predict")
def predict(house: HouseFeatures):
    try:
        input_data = pd.DataFrame({
            "MedInc": [house.MedInc],
            "HouseAge": [house.HouseAge],
            "AveRooms": [house.AveRooms],
            "AveBedrms": [house.AveBedrms],
            "Population": [house.Population],
            "AveOccup": [house.AveOccup],
            "Latitude": [house.Latitude],
            "Longitude": [house.Longitude]
        })
        predicted = model.predict(input_data)[0]
        price_usd=predicted*100000
        return {
            "predicted_price": f"${price_usd:,.2f}",
            "predicted_price_short": f"${price_usd / 1000:,.2f} hundred thousand",
            "confidence_range": f"${price_usd - 15000:,.2f} to ${price_usd + 15000:,.2f}"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )
@app.post("/predict_file")
async def predict_file(file: UploadFile = File(...)):
    
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are supported"
        )
    contents=await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    required_columns=[
        "MedInc", "HouseAge", "AveRooms", "AveBedrms", 
        "Population", "AveOccup", "Latitude", "Longitude"
    ]
    missing_columns=[
        col for col in required_columns
        if col not in df.columns
    ]
    if missing_columns:
        raise HTTPException(
            status_code=400,
            detail=f"these columns are missing from your file {missing_columns}"
        )
    if len(df)==0:
        raise HTTPException(
            status_code=400,
            detail="the uploaded file has no data rows"
        )
    try:
        predictions = model.predict(df[required_columns])

        df["predicted_price_usd"] = predictions * 100000

        df["predicted_price_usd"] = df["predicted_price_usd"].apply(
    lambda x: f"${x:,.0f}"
)
        output=df.to_csv(index=False)
        return StreamingResponse(
            io.StringIO(output),
            media_type="text/csv",
            headers={
                "content-disposition":"attachment; filename=predictions.csv"
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )