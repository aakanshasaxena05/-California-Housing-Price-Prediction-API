# California Housing Price Prediction API

## Project Overview

The California Housing Price Prediction API is a Machine Learning and FastAPI project that predicts California house prices using a trained Random Forest Regressor model.

The project uses the California Housing dataset and converts the trained Machine Learning model into a REST API using FastAPI.

Users can make predictions for a single house by sending JSON data or predict multiple houses by uploading a CSV file.

The project demonstrates the complete workflow of a Machine Learning deployment project, starting from dataset exploration and model training to API development and prediction.

## Project Objectives

The main objectives of this project are:

- Train a Machine Learning regression model
- Use Random Forest Regressor for house price prediction
- Save the trained model using Joblib
- Build a REST API using FastAPI
- Validate input data using Pydantic
- Predict the price of a single house
- Upload a CSV file for multiple predictions
- Generate a downloadable prediction CSV
- Provide interactive API documentation using Swagger
- Implement error handling and input validation

## Machine Learning Model

Algorithm used:

Random Forest Regressor

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to make predictions. It is suitable for regression problems where the target value is continuous, such as house prices.

The model is trained using the California Housing dataset.

## Input Features

The model uses the following eight features:

| Feature | Description |
|---|---|
| MedInc | Median income in the block group |
| HouseAge | Median house age in the block group |
| AveRooms | Average number of rooms per household |
| AveBedrms | Average number of bedrooms per household |
| Population | Block group population |
| AveOccup | Average household occupancy |
| Latitude | Geographic latitude |
| Longitude | Geographic longitude |

Target variable:

MedHouseVal

The California Housing target is represented in units of $100,000.

The API converts the prediction into an approximate US dollar value using:

price_usd = predicted × 100000

For example:

Model prediction = 2.5

Approximate house value = 2.5 × $100,000 = $250,000

## Dataset

The project uses the California Housing dataset.

The dataset contains information about housing districts in California, including income, house age, rooms, bedrooms, population, occupancy, latitude, longitude, and median house value.

For API testing, a CSV file containing 300 housing records can be used.

The CSV file used for prediction must contain these eight input columns:

MedInc
HouseAge
AveRooms
AveBedrms
Population
AveOccup
Latitude
Longitude

The target column MedHouseVal is not required when making predictions because the API generates the prediction.

## Project Structure

project1/

├── explore.py

├── train.py

├── main.py

├── house_features.joblib

├── house_model.joblib

├── predictions.csv

├── requirements.txt

└── test.csv

## File Description

explore.py

Used for exploring and understanding the California Housing dataset before model training.

train.py

Used to prepare the data, train the Random Forest Regressor, and save the trained model.

main.py

Contains the FastAPI application, model loading, validation, prediction endpoints, file upload functionality, and error handling.

house_model.joblib

Contains the trained Random Forest Regression model.

house_features.joblib

Contains the feature names used by the Machine Learning model.

predictions.csv

Contains prediction results generated from the bulk prediction endpoint.

requirements.txt

Contains all Python packages required to run the project.

README.md

Contains documentation and information about the project.

## Technologies Used

Python

Pandas

Scikit-learn

Random Forest Regressor

Joblib

FastAPI

Uvicorn

Pydantic

REST API

Swagger UI

OpenAPI

## Installation

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

.\venv\Scripts\Activate.ps1

Install the required packages:

pip install -r requirements.txt

Example requirements.txt:

fastapi
uvicorn
pandas
scikit-learn==1.9.1
joblib
python-multipart
openpyxl

The Scikit-learn version should match the version used when the model was trained and saved.

## Running the Application

Start the FastAPI server using:

python -m uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000

The application should display:

INFO: Uvicorn running on http://127.0.0.1:8000

INFO: Application startup complete.

## API Documentation

FastAPI automatically creates interactive API documentation.

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

Swagger UI allows users to view and test all API endpoints directly from the browser.

## API Endpoints

### 1. Home Endpoint

Method:

GET /

Purpose:

Checks whether the API is running.

Example response:

{
    "message": "California house price prediction api",
    "status": "running",
    "endpoint": "send POST request to /predict/"
}

### 2. Health Check Endpoint

Method:

GET /health

Purpose:

Checks the API and Machine Learning model status.

The endpoint returns information about the model and features.

### 3. Single House Prediction

Method:

POST /predict

Purpose:

Predicts the price of one house.

Example request:

{
    "MedInc": 8.3,
    "HouseAge": 25,
    "AveRooms": 6.2,
    "AveBedrms": 1.1,
    "Population": 1200,
    "AveOccup": 3.0,
    "Latitude": 34.2,
    "Longitude": -118.3
}

The API validates the input using Pydantic and sends the values to the trained Random Forest model.

Example response:

{
    "predicted_price": "$425,000.00",
    "predicted_price_short": "$425.00 hundred thousand",
    "confidence_range": "$410,000.00 to $440,000.00"
}

The confidence_range displayed by the current application is a fixed range around the prediction and is not a statistically calibrated prediction interval.

### 4. Bulk CSV Prediction

Method:

POST /predict_file

Purpose:

Predicts house prices for multiple records from a CSV file.

The CSV file must contain:

MedInc
HouseAge
AveRooms
AveBedrms
Population
AveOccup
Latitude
Longitude

Example CSV:

MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude
8.3,25,6.2,1.1,1200,3.0,34.2,-118.3
5.7,18,5.8,1.0,950,2.8,35.1,-117.9
3.2,30,4.9,1.2,700,2.5,36.4,-121.2

The API processes every row and creates a new column:

predicted_price_usd

The output is returned as:

predictions.csv

## Project Workflow

California Housing Dataset
        |
        v
explore.py
        |
        v
Data Exploration
        |
        v
train.py
        |
        v
Random Forest Regressor
        |
        v
Model Training
        |
        v
house_model.joblib
        |
        v
main.py
        |
        v
FastAPI Application
        |
        +----------------------+
        |                      |
        v                      v
    /predict            /predict_file
        |                      |
        v                      v
  Single JSON              CSV File
        |                      |
        +----------+-----------+
                   |
                   v
          Random Forest Model
                   |
                   v
            Price Prediction
                   |
                   v
          JSON Response / CSV

## Input Validation

The API uses Pydantic to validate incoming data.

For example:

MedInc: float = Field(gt=0)

This means MedInc must be a number greater than zero.

Latitude is validated between 32 and 42.

Longitude is validated between -125 and -114.

This validation helps prevent invalid values from being sent to the Machine Learning model.

## Error Handling

The API uses HTTPException to handle errors.

The API checks whether the uploaded file is a CSV.

It checks whether all required columns are available.

It checks whether the uploaded file contains data rows.

It also handles errors that may occur during prediction.

Examples of errors include:

Only CSV files are supported

Required columns are missing

The uploaded file has no data rows

Prediction failed

## Model Saving and Loading

The trained model is saved using Joblib.

Example:

joblib.dump(model, "house_model.joblib")

The model is loaded when the FastAPI application starts:

model = joblib.load("house_model.joblib")

The feature names are also loaded:

features = joblib.load("house_features.joblib")

This allows the API to use the trained model without retraining it every time the server starts.

## Testing with 300 Records

The API can be tested using a CSV file containing 300 California Housing records.

The process is:

300 Housing Records
        |
        v
CSV File
        |
        v
POST /predict_file
        |
        v
Validate CSV
        |
        v
Random Forest Model
        |
        v
300 Predictions
        |
        v
predictions.csv

This demonstrates how the API can process multiple housing records in one request.

## How to Test the API

Open the Swagger documentation:

http://127.0.0.1:8000/docs

To test the single prediction endpoint:

1. Open POST /predict
2. Click Try it out
3. Enter the house information
4. Click Execute
5. View the predicted price

To test bulk prediction:

1. Open POST /predict_file
2. Click Try it out
3. Upload a CSV file
4. Click Execute
5. Download the generated predictions.csv file

## Learning Outcomes

This project provides practical experience in:

Python programming

Machine Learning

Regression

Random Forest

Pandas

Data preprocessing

Scikit-learn

Model training

Joblib

Model serialization

FastAPI

REST API development

GET and POST requests

Pydantic

Data validation

File uploads

CSV processing

Exception handling

Swagger documentation

Machine Learning model deployment

## Future Improvements

The project can be improved by adding:

Excel file upload support

Streamlit frontend

Database integration

User authentication

Docker support

Cloud deployment

Automated model evaluation

Unit testing

API logging

Model monitoring

Model versioning

Automated model retraining

Properly calibrated prediction intervals

## Author

Aakansha Saxena

Skills Demonstrated:

Python
Machine Learning
Pandas
Scikit-learn
Random Forest
FastAPI
REST API
Pydantic
Joblib
Data Processing
Model Deployment

## Conclusion

The California Housing Price Prediction API demonstrates how a Machine Learning model can be trained, saved, and deployed as a REST API.

The project uses a Random Forest Regressor to predict California house prices based on income, house age, rooms, bedrooms, population, occupancy, latitude, and longitude.

The FastAPI application provides endpoints for single-house prediction and bulk CSV prediction. Pydantic is used for input validation, Pandas is used for data processing, and Joblib is used for saving and loading the trained Machine Learning model.

This project provides practical experience in both Machine Learning and backend API development and demonstrates the complete process of deploying a Machine Learning model through FastAPI.
