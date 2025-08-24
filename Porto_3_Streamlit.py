import streamlit as st
import pandas as pd
import joblib

st.title("Churn Prediction")

st.write("Ini adalah App untuk memprediksi apakah seseorang akan churn atau tidak")

model = joblib.load("Model Porto 3.joblib")

def get_prediction(data:pd.DataFrame):
    pred = model.predict(data)
    pred_proba = model.predict_proba(data)
    return pred, pred_proba

st.subheader("Data Customer")

CreditScore = st.number_input("Credit Score", min_value=0.0, value=0.0)
Geography = st.selectbox("Di mana Countrynya?", ["Germany", "France", "Spain"])
Gender = st.selectbox("Jenis Kelamin", ["Female", "Male"])
Age = st.number_input("Usia (Harus 18 ke atas)", min_value=18.0, value=18.0)
Tenure = st.number_input("Sudah berapa lama menjadi customer? (Tahun)", min_value=0.0, value=0.0)
Balance = st.number_input("Saldo", min_value=0.0, value=0.0)
NumofProducts = st.slider("Jumlah Produk yang dimiliki", min_value=1.0, max_value=4.0, value=1.0, step=1.0)
HasCrCard = st.selectbox("Apakah mempunyai kartu kredit?", ["Ya", "Tidak"])
HasCrCard = 1 if HasCrCard == "Ya" else 0
IsActiveMember = st.selectbox("Apakah masih menjadi member aktif?", ["Ya", "Tidak"])
IsActiveMember = 1 if IsActiveMember == "Ya" else 0
EstimatedSalary = st.number_input("Berapa estimasi gajinya?", min_value=0.0, value=0.0)

data = pd.DataFrame({"CreditScore": [CreditScore],
                     "Geography": [Geography],
                     "Gender": [Gender],
                     "Age": [Age],
                     "Tenure": [Tenure],
                     "Balance": [Balance],
                     "NumOfProducts": [NumofProducts],
                     "HasCrCard": [HasCrCard],
                     "IsActiveMember": [IsActiveMember],
                     "EstimatedSalary": [EstimatedSalary]})

button = st.button("Predict", use_container_width=True)

if button:
    st.write("Prediksi Berhasil !")
    pred, pred_proba = get_prediction(data)
    
    label_map = {0: "Tidak Churn", 1: "Churn"}
    label_pred = label_map[pred[0]]
    label_proba = pred_proba[0][pred[0]]
    output = f"Customer diklasifikasikan sebagai {label_proba:.0%} {label_pred}"
    st.write(output)