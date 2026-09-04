# 🛒 Superstore Real-Time Sales Dashboard

An interactive, real-time sales dashboard built with **Python, Streamlit, and Plotly**, analyzing ~10,000 retail transactions (2014–2017) across regions, categories, and products.

## 🌐 Live Demo
👉 [Add your Streamlit Cloud link here after deployment]

## 📊 Features
- 💰 **KPI Cards** — Total Sales, Total Profit, Orders, Profit Margin
- 🔍 **Interactive Filters** — Region, Category, and Year (all charts update instantly)
- 📅 **Monthly Sales Trend** — line chart of revenue over time
- 📦 **Category Analysis** — Sales vs Profit comparison
- 🗺️ **Regional Breakdown** — Sales share by region (donut chart)
- 🏆 **Top 10 Products** — Best-selling products ranked
- 📋 **Data Explorer** — View the filtered raw data

## 🧰 Tech Stack
| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data cleaning & aggregation |
| Streamlit | Web app framework |
| Plotly Express | Interactive charts |

## 📁 Project Structure
- `analysis.py` — Data loading, cleaning & EDA
- `dashboard.py` — Streamlit dashboard app
- `cleaned_data.csv` — Processed dataset (9,994 records)
- `requirements.txt` — Python dependencies

## 🔑 Key Insights
- 🥇 **West region** leads in sales (~$725K)
- 💻 **Technology** is the most profitable category
- 🖨️ **Copiers** generate the highest profit ($55K+)
- 📉 **Tables** lose money (-$17K) — a candidate for pricing review

## 🚀 Run Locally
pip install -r requirements.txt
streamlit run dashboard.py



## 📈 Future Improvements
- Real-time order simulation with auto-refresh
- Sales forecasting with machine learning
- Customer segmentation analysis

---
*Dataset: Superstore Sales from Kaggle*

