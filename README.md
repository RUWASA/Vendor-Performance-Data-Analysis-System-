# Vendor-Performance-Data-Analysis-System-

📊 **Interactive Dashboard to Analyze Vendor Performance, Predict Delays, and Monitor Quality**

## 🔹 Overview
This project is a **Vendor Performance Analytics System** built using **Python, Pandas, Seaborn, Matplotlib, and Streamlit**.  
It helps businesses:
- Evaluate vendor reliability, cost efficiency, and quality.
- Forecast potential delivery delays using machine learning.
- Visualize key metrics for informed decision-making.
- Provide interactive dashboards for performance insights.

## 🔹 Features
1. **Vendor Overview**
   - View vendor details, category, location, and ratings.
2. **Purchase Order Analysis**
   - Average delivery days per vendor.
   - Total spend per vendor and insights into purchase patterns.
3. **Quality Analysis**
   - Visualize quality check scores and defects found.
   - Identify vendors with consistent quality issues.
4. **Delay Predictions**
   - Predict the probability of vendor delays using ML models.
   - Display risk levels for proactive management.
5. **Vendor Risk Summary**
   - Visual summary of vendors with high delay risk.
   - Interactive bar charts for quick insights.

## 🔹 Tech Stack
- **Python** – Core programming
- **Pandas** – Data manipulation
- **Seaborn & Matplotlib** – Data visualization
- **Streamlit** – Interactive web dashboard
- **Machine Learning** – Predictive modeling for vendor delays

## 🔹 Installation
1. Clone the repository:
```bash
[git clone https://github.com/RUWASA/Vendor-Performance-Data-Analysis-System-](url)

2.Navigate to the project folder:
cd vendor_performance_system

3.Install dependencies:
pip install -r requirements.txt

4.Run the Streamlit app:
streamlit run app.py

🔹 Repository Structure
├── app.py                 # Main Streamlit app
├── model_training.py      # ML model for delay prediction
├── requirements.txt       # Python dependencies
├── predictions.csv        # ML predictions
├── quality_checks.csv     # Quality check data
├── sample_purchase_orders.csv
├── sample_scoring_data.csv
├── sample_training_data.csv
├── vendors.csv            # Vendor master data
└── README.md              # Project documentation


🔹 Usage
The dashboard opens in your browser at http://localhost:8501.
Navigate through different sections: Vendor Overview, Purchase Orders, Quality Analysis, Delay Predictions, and Vendor Risk Summary.
Upload or modify CSV files to update the dashboard dynamically.

🔹 Live Demo
Check out the live interactive dashboard here:
[https://iutkcpynl3vkbudxdbagrr.streamlit.app/](url)

