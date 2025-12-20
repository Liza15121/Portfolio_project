## Car Resale Price Prediction App
This Streamlit application predicts the resale price of cars based on user inputs and displays matching cars from the dataset. It is designed to be user-friendly and visually appealing, making it easy to get instant resale estimates and explore similar vehicles.

**Features**
•	Predicts resale price using a pre-trained machine learning model.
•	Displays matching cars from the dataset based on user input.
•	Interactive UI with sidebar controls for easy input.
•	Clean, responsive layout with custom styling.

**Installation**
1. Clone the repository
git clone https://github.com/yourusername/car-resale-prediction.git
cd car-resale-prediction

2. Install the required packages:
pip install -r requirements.txt

3. Ensure you have the following files in the project directory:
•	`car_pred_model` (your trained model file)
•	`Cars24.csv` (dataset file)
•	(Optional) `car_logo.png` for the app logo

**Usage**
1. Run the Streamlit app:
streamlit run app.py

2. Use the sidebar to select car details:
•	Fuel type
•	Seller type
•	Engine power
•	Transmission type
•	Number of seats

3. Click “Predict Price” to see the predicted resale price and matching cars.

**Dataset**
The dataset used is `Cars24.csv`, which contains car details such as make, model, year, fuel type, seller type, transmission, engine power, seats, and kilometers driven.

**Model**
The prediction model (`car_pred_model`) is a pre-trained machine learning model loaded using Pickle. It uses features like year, seller type, kilometers driven, fuel type, transmission, engine power, and seats for prediction.

**Customization**
•	Add your own logo by replacing `cars.jpg`.
•	Customize colors and layout by editing the CSS in the app.

**Contributing**
Feel free to open issues or submit pull requests for improvements or new features.
