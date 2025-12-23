import streamlit as st
import pandas as pd
import pickle

#load the model from disk
with open('./artefactes/car_pred', 'rb') as f:
    model = pickle.load(f)   

cars_df = pd.read_csv("./artefactes/Cars24.csv")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Car Resale Price Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #666;'>Get the best resale price estimate and matching cars!</h3>", unsafe_allow_html=True)


#Usage of emojis for better visual appeal
from PIL import Image
logo = Image.open("./artefactes/ cars24.jpg")
st.sidebar.image(logo, width=250)

st.dataframe(cars_df.head())

## Encoding Categorical features
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
            }


col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select the fuel type",
                           ["Diesel", "Petrol", "CNG", "LPG", "Electric"])

engine = col1.slider("Set the Engine Power",
                     500, 6750, step=100)

seats = col2.selectbox("Enter the number of seats",
                       [4,5,7,8])

km_driven = col2.slider("Set the Kms Driven",
                        5000, 500000, step=5000)

transmission_type = st.sidebar.radio("Select the transmission type",
                                   ["Manual", "Automatic"])

seller_type = st.sidebar.selectbox("Select the seller type",
                             ["Dealer", "Individual", "Trustmark Dealer"])

year_since_manufacture = st.sidebar.selectbox("Select the Year of Manufacture",
                                             [i for i in range(2009, 2024)])



if st.button("Predict Price"):
    encoded_fuel_type = encode_dict['fuel_type'][fuel_type]
    encoded_seller_type = encode_dict['seller_type'][seller_type]
    encoded_transmission_type = encode_dict['transmission_type'][transmission_type]


    input_features = [[year_since_manufacture, encoded_seller_type, km_driven, encoded_fuel_type, encoded_transmission_type, 19.7, engine, 46.3, seats]]

    price = round(max(0, model.predict(input_features)[0]), 2)

    st.write("🚗 Get the best resale price estimate!")
    
    st.header("Predicted price is: " + str(price) + " Lakhs INR")










    # Filter and display matching cars from the dataset
    #filtered_cars = cars_df[
        #(cars_df['fuel_type'] == fuel_type) &
        #(cars_df['seller_type'] == seller_type) &
        #(cars_df['transmission_type'] == transmission_type) &
        #(cars_df['seats'] == seats) &
        #(cars_df['engine'] >= engine - 100)  # Allowing a range of ±100 for engine power
        #                   ]


    #st.subheader("Matching Cars in Dataset:")
    #if not filtered_cars.empty:
        #st.dataframe(filtered_cars)
    #else:
        #st.write("No matching cars of your criteria.")




