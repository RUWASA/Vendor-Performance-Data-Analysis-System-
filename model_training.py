import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ============================
# 1. LOAD TRAINING DATA
# ============================
train = pd.read_csv("sample_training_data.csv")

X = train[["AvgDeliveryDays", "AvgQualityScore", "TotalSpend"]]
y = train["Delayed"]

# ============================
# 2. SPLIT DATA
# ============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ============================
# 3. SCALING
# ============================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ============================
# 4. TRAIN MODEL
# ============================
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# ============================
# 5. ACCURACY
# ============================
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# ============================
# 6. LOAD SCORING DATA
# ============================
score_df = pd.read_csv("sample_scoring_data.csv")

X_new = score_df[["AvgDeliveryDays", "AvgQualityScore", "TotalSpend"]]
X_new_scaled = scaler.transform(X_new)

# ============================
# 7. PREDICT DELAY PROBABILITY
# ============================
score_df["delay_probability"] = model.predict_proba(X_new_scaled)[:, 1]
score_df["delay_risk"] = score_df["delay_probability"].apply(
    lambda x: "HIGH" if x > 0.6 else "MEDIUM" if x > 0.3 else "LOW"
)

# ============================
# 8. SAVE PREDICTIONS
# ============================
score_df.to_csv("predictions.csv", index=False)

print("Predictions saved to predictions.csv")
