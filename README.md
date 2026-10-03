Yes. Here is a **clean, copy-paste-friendly `README.md`**. You can copy the entire block directly into GitHub without changing anything.

````markdown
# California Housing Price Prediction API

A Machine Learning based REST API built using FastAPI to predict California house prices.

The project uses a Random Forest Regressor trained on the California Housing dataset. The API supports both single house prediction and batch prediction using CSV files.

## Features

- House price prediction using Machine Learning
- Random Forest Regressor
- FastAPI REST API
- Pydantic input validation
- Single house prediction
- CSV batch prediction
- Automatic Swagger documentation
- Health check endpoint
- Error handling
- Joblib model loading

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pandas
- Scikit-learn
- Joblib
- Pydantic

## Machine Learning Model

The project uses:

```text
Random Forest Regressor
````

The trained model is saved using Joblib.

```text
house_model.joblib
```

The model features are stored in:

```text
house_features.joblib
```

## Input Features

The model uses the following features:

| Feature    | Description                              |
| ---------- | ---------------------------------------- |
| MedInc     | Median income in the block group         |
| HouseAge   | Median house age                         |
| AveRooms   | Average number of rooms per household    |
| AveBedrms  | Average number of bedrooms per household |
| Population | Block group population                   |
| AveOccup   | Average house occupancy                  |
| Latitude   | Block group latitude                     |
| Longitude  | Block group longitude                    |

## Project Structure

```text
house_prediction/
│
├── main.py
├── house_model.joblib
├── house_features.joblib
├── requirements.txt
├── housing.csv
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/aakanshasaxena05/house_prediction.git
```

Move into the project folder:

```bash
cd house_prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Requirements

Create a file named:

```text
requirements.txt
```

Add:

```text
fastapi
uvicorn
pandas
scikit-learn==1.9.1
joblib
python-multipart
```

## Run the API

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

### ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

### 1. Home Endpoint

```text
GET /
```

Checks whether the API is running.

Example response:

```json
{
    "message": "California house price prediction api",
    "status": "running",
    "endpoint": "send POST request to /predict/"
}
```

### 2. Health Check

```text
GET /health
```

Returns the API and model status.

Example:

```json
{
    "status": "running",
    "model": "Randomforestregressor"
}
```

### 3. Single House Prediction

```text
POST /predict
```

This endpoint predicts the price of a single house.

Example input:

```json
{
    "MedInc": 8.3,
    "HouseAge": 41,
    "AveRooms": 6.9,
    "AveBedrms": 1.0,
    "Population": 322,
    "AveOccup": 2.5,
    "Latitude": 37.88,
    "Longitude": -122.23
}
```

Example response:

```json
{
    "predicted_price": "$425,000.00",
    "predicted_price_short": "$4.25 hundred thousand",
    "confidence_range": "$410,000.00 to $440,000.00"
}
```

The actual prediction depends on the trained model and input values.

### 4. CSV Batch Prediction

```text
POST /predict_file
```

This endpoint accepts a CSV file containing multiple housing records.

Required columns:

```text
MedInc
HouseAge
AveRooms
AveBedrms
Population
AveOccup
Latitude
Longitude
```

The API processes all rows and returns a CSV file containing the predictions.

## Example CSV

```csv
MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude
8.3,41,6.9,1.0,322,2.5,37.88,-122.23
7.2,35,6.5,1.1,450,2.8,37.85,-122.20
5.6,30,5.8,1.0,390,2.6,37.80,-122.25
```

## Project Workflow

```text
California Housing Dataset
          ↓
Data Preprocessing
          ↓
Feature Selection
          ↓
Train Random Forest Model
          ↓
Save Model using Joblib
          ↓
Create FastAPI Application
          ↓
Load Trained Model
          ↓
Receive User Input
          ↓
Validate Input
          ↓
Generate Prediction
          ↓
Return JSON or CSV Response
```

## Input Validation

Pydantic is used to validate user input.

Example:

```python
MedInc: float = Field(gt=0)
```

This means that `MedInc` must be greater than zero.

Latitude is validated using:

```python
Latitude: float = Field(ge=32, le=42)
```

Longitude is validated using:

```python
Longitude: float = Field(ge=-125, le=-114)
```

## Error Handling

The API uses FastAPI's `HTTPException` to handle errors.

Example:

```python
raise HTTPException(
    status_code=400,
    detail="Only CSV files are supported"
)
```

The API handles errors such as:

* Invalid input
* Invalid CSV files
* Missing CSV columns
* Empty CSV files
* Prediction errors

## Model Saving

The trained model is saved using Joblib.

```python
joblib.dump(model, "house_model.joblib")
```

The saved model is loaded when the FastAPI application starts:

```python
model = joblib.load("house_model.joblib")
```

This allows the API to use the trained model without retraining it every time.

## Testing With 300 Records

The API can be tested using a CSV file containing 300 housing records.

The CSV file should contain:

```text
MedInc
HouseAge
AveRooms
AveBedrms
Population
AveOccup
Latitude
Longitude
```

Upload the file using:

```text
POST /predict_file
```

You can test the endpoint through Swagger:

```text
http://127.0.0.1:8000/docs
```

The API will process all records and return a CSV file containing the predicted prices.

## Important Note

The `confidence_range` currently returned by the API is a fixed range around the prediction.

It should not be considered a statistically calculated confidence interval unless a proper uncertainty estimation method has been implemented.

## Future Improvements

* Add Streamlit frontend
* Add database integration
* Add authentication
* Add Docker support
* Deploy the API to the cloud
* Add automated testing
* Add model performance metrics
* Add model monitoring
* Add prediction history
* Add Excel file support
* Add data visualization
* Add automated model retraining

## Learning Outcomes

This project demonstrates:

* Python programming
* Machine Learning
* Random Forest Regression
* Pandas
* Scikit-learn
* Model serialization
* Joblib
* FastAPI
* REST API development
* GET and POST requests
* Pydantic validation
* HTTP status codes
* Exception handling
* CSV processing
* Swagger documentation
* Batch prediction

## How to Run

```bash
python -m venv venv
```

Activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI application:

```bash
python -m uvicorn main:app --reload
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

## Author

Aakansha Saxena

MCA Student | Python | Machine Learning | Data Science | FastAPI

GitHub:

[https://github.com/aakanshasaxena05](https://github.com/aakanshasaxena05)

## Conclusion

The California Housing Price Prediction API is an end-to-end Machine Learning project that demonstrates how a trained Machine Learning model can be deployed as a REST API using FastAPI.

The project supports both individual house price prediction and batch prediction using CSV files.


Would you like a shorter recruiter-focused version or a more polished portfolio-style version?
