import streamlit as st
import pickle
import pandas as pd


model = pickle.load(open("churn_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("Customer Churn Prediction")

st.write("Enter Customer Details:")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.number_input("Tenure", min_value=0)
monthly_charges = st.number_input("Monthly Charges")
total_charges = st.number_input("Total Charges")

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

# Convert input into dictionary
input_data = {
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
}

# Encoding (must match training)
input_data["gender_Male"] = 1 if gender == "Male" else 0
input_data["Contract_One year"] = 1 if contract == "One year" else 0
input_data["Contract_Two year"] = 1 if contract == "Two year" else 0

# Convert to DataFrame
input_df = pd.DataFrame([input_data])


input_df = input_df.reindex(columns=columns, fill_value=0)

# Prediction
if st.button("Predict"):
    pred = model.predict(input_df)

    if pred[0] == 1:
        st.error(" Customer will Churn")
    else:
        st.success(" Customer will Stay")

