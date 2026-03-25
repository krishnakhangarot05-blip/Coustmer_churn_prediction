import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("churn_model.pkl", "rb"))

st.title("Customer Churn Prediction")

st.write("Enter Customer Details:")


gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.number_input("Tenure (months)", min_value=0)
monthly_charges = st.number_input("Monthly Charges")
total_charges = st.number_input("Total Charges")

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

#encoding
gender = 1 if gender == "Male" else 0

contract_one = 1 if contract == "One year" else 0
contract_two = 1 if contract == "Two year" else 0


if st.button("Predict"):
    data = np.array([[gender, tenure, monthly_charges, total_charges,
                      contract_one, contract_two]])

    pred = model.predict(data)

    if pred[0] == 1:
        st.error(" Customer will Churn")
    else:
        st.success(" Customer will Stay")
