
<h3>Files</h3>
<dl>
<dt>analysis.ipynb</dt>
<dd>carried out the data analysis such as factor analysis,clustering,visualisation etc.</dd>
<dt>customer_profile.py</dt>
<dd>streamlit app for checking the customer profiles, adding new customers etc.</dd>
<dt>fa.pkl</dt>
<dd>factor analysis object created in analysis.ipynb</dd>
<dt>scaler.ipynb</dt>
<dd>standard scaler object</dd>
<dt>significantfeatures.pkl</dt>
<dd>list all the factors and the attributes they have high positive or negative correlation with</dd>
</dl>
<h4>CLUSTER LABELS (check images folder for better understanding)</h4>

Cluster 0: Low Factor 4

Cluster 1: Moderate for all Factors

Cluster 2: High Factor 5 Moderate for other Factors

Cluster 3: Low Factor 3 Moderate for other factors

Cluster 4: High Factor 2 and Factor 3 Moderate for remaining Factors

Cluster 5: High Factor 1 and Factor 4 Moderate for remaining Factors


<h4>FACTORS (check images/factor correlation heatmap )</h4>

Factor 1:
positive correlation: ['PURCHASES', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES', 'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_TRX', 'PAYMENTS', 'monthly_average_purchase', 'monthly_average_payments'] 
negative correlation: []

Factor 2:
positive correlation: ['CASH_ADVANCE', 'CASH_ADVANCE_TRX', 'PAYMENTS', 'monthly_average_payments']
negative correlation: []

Factor 3:
positive correlation: [] 
negative correlation: ['BALANCE', 'balance_to_creditlimit_ratio']

Factor 4:
positive correlation: []
negative correlation: ['PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY']

Factor 5: 
positive correlation: ['CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX'] 
negative correlation: []

<b>NOTE:</b> attributes provided in the dataset are in uppercase whereas derived KPIs are in lowercase