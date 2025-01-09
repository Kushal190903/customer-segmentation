<h3>Files</h3>
<dl>
  <dt>analysis.ipynb</dt>
  <dd>Carried out the data analysis such as factor analysis, clustering, visualization, etc.</dd>
  <dt>app.py</dt>
  <dd>Streamlit app for checking the customer profiles, adding new customers, etc.</dd>
  <dt>fa.pkl</dt>
  <dd>Factor analysis object created in analysis.ipynb.</dd>
  <dt>scaler.pkl</dt>
  <dd>Standard scaler object.</dd>
  <dt>significantfeatures.pkl</dt>
  <dd>List of all the factors and the attributes they have high positive or negative correlation with.</dd>
</dl>

<h4>CLUSTER LABELS (check images folder for better understanding)</h4>
<ul>
  <li><strong>Cluster 0:</strong> Low Factor 4</li>
  <li><strong>Cluster 1:</strong> Moderate for all Factors</li>
  <li><strong>Cluster 2:</strong> High Factor 5, Moderate for other Factors</li>
  <li><strong>Cluster 3:</strong> Low Factor 3, Moderate for other Factors</li>
  <li><strong>Cluster 4:</strong> High Factor 2 and Factor 3, Moderate for remaining Factors</li>
  <li><strong>Cluster 5:</strong> High Factor 1 and Factor 4, Moderate for remaining Factors</li>
</ul>

<h4>FACTORS (check images/factor correlation heatmap)</h4>

<p><strong>Factor 1:</strong></p>
<ul>
  <li><strong>Positive correlation:</strong> PURCHASES, ONEOFF_PURCHASES, INSTALLMENTS_PURCHASES, ONEOFF_PURCHASES_FREQUENCY, PURCHASES_TRX, PAYMENTS, monthly_average_purchase, monthly_average_payments</li>
  <li><strong>Negative correlation:</strong> None</li>
</ul>

<p><strong>Factor 2:</strong></p>
<ul>
  <li><strong>Positive correlation:</strong> CASH_ADVANCE, CASH_ADVANCE_TRX, PAYMENTS, monthly_average_payments</li>
  <li><strong>Negative correlation:</strong> None</li>
</ul>

<p><strong>Factor 3:</strong></p>
<ul>
  <li><strong>Positive correlation:</strong> None</li>
  <li><strong>Negative correlation:</strong> BALANCE, balance_to_creditlimit_ratio</li>
</ul>

<p><strong>Factor 4:</strong></p>
<ul>
  <li><strong>Positive correlation:</strong> None</li>
  <li><strong>Negative correlation:</strong> PURCHASES_FREQUENCY, PURCHASES_INSTALLMENTS_FREQUENCY</li>
</ul>

<p><strong>Factor 5:</strong></p>
<ul>
  <li><strong>Positive correlation:</strong> CASH_ADVANCE_FREQUENCY, CASH_ADVANCE_TRX</li>
  <li><strong>Negative correlation:</strong> None</li>
</ul>

<p><strong>NOTE:</strong> Attributes provided in the dataset are in uppercase, whereas derived KPIs are in lowercase.</p>
