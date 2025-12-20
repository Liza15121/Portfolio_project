# Car Resale Price Prediction App

This Streamlit application predicts the resale price of cars based on user inputs such as fuel type, seller type, engine power, transmission type, number of seats, and kilometers driven. It also displays matching cars from the dataset based on the user's selected criteria.

## Features

- Predicts resale price using a pre-trained machine learning model.
- Filters and displays cars matching the user’s input details.
- Interactive UI for easy input and result viewing.

## Prerequisites

- Python 3.7 or higher
- Streamlit
- Pandas
- Pickle

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/car-resale-prediction.git
   cd car-resale-prediction
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have the following files in the project directory:
   - `car_pred_model` (your trained model file)
   - `Cars24.csv` (dataset file)

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Use the UI to select car details:
   - Fuel type
   - Seller type
   - Engine power
   - Transmission type
   - Number of seats
   - Kilometers driven

3. Click "Predict Price" to see the predicted resale price and matching cars from the dataset.

## Dataset

The dataset used is `Cars24.csv`, which contains car details such as make, model, year, fuel type, seller type, transmission, engine power, seats, and kilometers driven.

## Model

The prediction model (`car_pred_model`) is a pre-trained machine learning model loaded using Pickle. It uses features like year, seller type, kilometers driven, fuel type, transmission, engine power, and seats for prediction.

## Contributing

Feel free to open issues or submit pull requests for improvements or new features.

***

