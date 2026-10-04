import streamlit as st
import requests



API_URL = "http://backend:8000/predict"

st.title("Telco Customer Churn Prediction")
st.divider()
st.write("Enter customer details to estimate the likelihood of customer churn.")
st.subheader("Customer Information")
st.caption("Basic customer and account details")

gender = st.selectbox("Gender", ["Female", "Male"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=12)

st.subheader("Service Information")
st.caption("Services currently used by the customer")
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

st.subheader("Billing & Contract")
st.caption("Contract and billing details")
contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

st.subheader("Support & Tickets")
st.caption("Customer support activity")
num_admin_tickets = st.number_input(
    "Number of Admin Tickets",
    min_value=0,
    value=0
)

num_tech_tickets = st.number_input(
    "Number of Tech Tickets",
    min_value=0,
    value=0
)


st.divider()
st.subheader("Prediction Result")
if st.button("Predict Churn", type="primary"):
    customer_data = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "numAdminTickets": num_admin_tickets,
        "numTechTickets": num_tech_tickets
    }

    response = requests.post(API_URL, json=customer_data)
    result = response.json()

    if result["churn_prediction"] == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer is unlikely to churn")

    st.metric(
        "Churn Probability",
        f"{result['churn_probability'] * 100:.2f}%"
    )

    st.caption("Probability above 40% is classified as churn.")