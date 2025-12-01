import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Vendor Performance System", layout="wide")

# =============================
# LOAD DATA
# =============================
purchase = pd.read_csv("sample_purchase_orders.csv")
train = pd.read_csv("sample_training_data.csv")
score = pd.read_csv("sample_scoring_data.csv")
vendors = pd.read_csv("vendors.csv")
qc = pd.read_csv("quality_checks.csv")
pred = pd.read_csv("predictions.csv")

st.title("📊 Vendor Performance Data Analysis System")

# ----------------------------
# SECTION 1: Vendor Overview
# ----------------------------
st.header("1️⃣ Vendor Overview")

st.dataframe(vendors)

# ----------------------------
# SECTION 2: Purchase Order Analysis
# ----------------------------
st.header("2️⃣ Purchase Order Insights")

st.write("### Average Delivery Days per Vendor")
avg_delivery = purchase.groupby("VendorID")["DeliveryDays"].mean()

st.bar_chart(avg_delivery)

# ----------------------------
# SECTION 3: Quality Analysis
# ----------------------------
st.header("3️⃣ Quality Check Insights")

fig, ax = plt.subplots()
sns.scatterplot(data=qc, x="defects_found", y="quality_score", ax=ax)
st.pyplot(fig)

# ----------------------------
# SECTION 4: Delay Predictions (ML Output)
# ----------------------------
st.header("4️⃣ Delay Prediction Results (Machine Learning)")

pred_display = pred[["VendorID", "AvgDeliveryDays", "AvgQualityScore",
                     "TotalSpend", "delay_probability", "delay_risk"]]

st.dataframe(pred_display)

# ----------------------------
# SECTION 5: Vendor Risk Summary
# ----------------------------
st.header("5️⃣ Vendor Risk Summary")

risk_count = pred["delay_risk"].value_counts()
st.bar_chart(risk_count)
