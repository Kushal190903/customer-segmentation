import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the necessary files
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
with open('fa.pkl', 'rb') as file:
    fa = pickle.load(file)
with open('significantfeatures.pkl', 'rb') as file:
    factorlabels = pickle.load(file)
with open('cluster_model.pkl','rb') as file:
    kmeans=pickle.load(file)

# Load data
customerdataframes = pd.read_csv(r'C:\Users\HP\Desktop\vs_projects\softsensor assignment\Data_problem  1.csv')
clusterlabels = {
    0: 'Low Factor 4',
    1: 'Moderate for all Factors',
    2: 'High Factor 5 \nModerate for other Factors',
    3: 'Low Factor 3\nModerate for other factors',
    4: 'High Factor 2 and Factor 3\nModerate for remaining Factors',
    5: 'High Factor 1 and Factor 4\nModerate for remaining Factors'
}

# Derived KPI calculation function
def calculate_kpis(data):

    data['monthly_average_purchase'] = data['PURCHASES'] / data['TENURE']
    data['monthly_average_payments'] = data['PAYMENTS'] / data['TENURE']
    data['balance_to_creditlimit_ratio'] = data['BALANCE'] / data['CREDIT_LIMIT']

   

    # Handle potential division-by-zero or NaN values
    data.replace([np.inf, -np.inf], np.nan, inplace=True)
    data.fillna(0, inplace=True)
    return data

# Fit the cluster for a new customer
def predict_cluster(new_customer_data):
    scaled_data = scaler.transform(new_customer_data)
    factor_data = fa.transform(scaled_data)
    cluster = kmeans.predict(factor_data)
    return cluster[0]

# Streamlit App
st.title("Customer Clustering and Profile Analysis")

# Sidebar
st.sidebar.title("Cluster and Factor Labels")
st.sidebar.subheader("Cluster Labels")
for i, label in clusterlabels.items():
    st.sidebar.write(f"Cluster {i}: {label}")

st.sidebar.subheader("Factor Labels")
for i, label in factorlabels.items():
    st.sidebar.write(f"Factor {i}: {label}")

# Displaying current data
st.subheader("Customer Data")
customerdataframes = calculate_kpis(customerdataframes)
st.write(customerdataframes)

# Adding new customer
st.subheader("Add a New Customer")
new_customer = {}
columns = ['BALANCE', 'BALANCE_FREQUENCY', 'PURCHASES', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES',
           'CASH_ADVANCE', 'PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY',
           'CASH_ADVANCE_FREQUENCY', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT', 'TENURE']

for col in columns:
    new_customer[col] = st.number_input(f"Enter {col}", min_value=0.0, step=0.1)

if st.button("Add and Analyze New Customer"):
    new_customer_df = pd.DataFrame([new_customer])
    new_customer_df = calculate_kpis(new_customer_df)
    cluster = predict_cluster(new_customer_df.drop(columns=['CUST_ID'], errors='ignore'))
    st.write(f"The new customer fits into **Cluster {cluster}: {clusterlabels[cluster]}**")

    st.subheader("Customer KPIs")
    st.write(new_customer_df[['monthly_average_purchase', 'monthly_average_payments', 'balance_to_creditlimit_ratio']])

# Check existing customer profile
st.subheader("Check Customer Profile")
customer_id = st.text_input("Enter Customer ID")

if st.button("Fetch Profile"):
    if customer_id in customerdataframes['CUST_ID'].values:
        customer_profile = customerdataframes[customerdataframes['CUST_ID'] == customer_id]
        cluster = predict_cluster(customer_profile.drop(columns=['CUST_ID'], errors='ignore'))
        st.write(f"The customer belongs to **Cluster {cluster}: {clusterlabels[cluster]}**")
        st.subheader('Customer Profile')
        st.write(customer_profile)
        st.subheader("Customer KPIs")
        
        kpi_Data=pd.DataFrame()
        kpi_Data[['monthly_average_purchase', 'monthly_average_payments', 'balance_to_creditlimit_ratio']]=customer_profile[['monthly_average_purchase', 'monthly_average_payments', 'balance_to_creditlimit_ratio']]
        kpi_Data['credit_utilization_ratio'] = customer_profile['CASH_ADVANCE'] /customer_profile['CREDIT_LIMIT']

        kpi_Data['oneoff_to_total_purchase_ratio'] = customer_profile['ONEOFF_PURCHASES'] / customer_profile['PURCHASES']
        
        kpi_Data['payment_to_minimum_ratio'] =customer_profile['PAYMENTS'] / customer_profile['MINIMUM_PAYMENTS']
        kpi_Data.replace([np.inf, -np.inf], np.nan, inplace=True)
        kpi_Data.fillna(0, inplace=True)
        st.write(kpi_Data)
    else:
        st.error("Customer ID not found in the dataset.")
