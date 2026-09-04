import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Superstore Dashboard", layout="wide")
st.title("🛒 Superstore Sales Dashboard")

# ===== LOAD DATA =====
df = pd.read_csv("cleaned_data.csv", parse_dates=["Order Date", "Ship Date"])

# ===== FILTERS =====
st.sidebar.header("🔍 Filters")
regions = st.sidebar.multiselect("Region(s)", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))
categories = st.sidebar.multiselect("Category(s)", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
years = st.sidebar.multiselect("Year(s)", sorted(df["Year"].unique()), default=sorted(df["Year"].unique()))

dff = df[df["Region"].isin(regions) & df["Category"].isin(categories) & df["Year"].isin(years)]

if dff.empty:
    st.warning("⚠️ No data — select at least one option in each filter.")
    st.stop()

# ===== KPIs =====
c1, c2, c3, c4 = st.columns(4)
c1.metric("💰 Total Sales", f"${dff['Sales'].sum():,.0f}")
c2.metric("📈 Total Profit", f"${dff['Profit'].sum():,.0f}")
c3.metric("🧾 Orders", f"{dff['Order ID'].nunique():,}")
c4.metric("🎯 Margin", f"{dff['Profit'].sum()/dff['Sales'].sum()*100:.1f}%")

# ===== CHART 1: Monthly Trend =====
trend = dff.groupby(dff["Order Date"].dt.to_period("M"))["Sales"].sum().reset_index()
trend.columns = ["Month", "Sales"]
trend["Month"] = trend["Month"].astype(str)
st.plotly_chart(px.line(trend, x="Month", y="Sales", markers=True, title="📅 Monthly Sales Trend"), use_container_width=True)

# ===== CHART 2 & 3 side by side =====
col1, col2 = st.columns(2)

cat = dff.groupby("Category")[["Sales", "Profit"]].sum().reset_index()
col1.plotly_chart(px.bar(cat, x="Category", y=["Sales", "Profit"], barmode="group", title="📦 Category: Sales vs Profit"), use_container_width=True)

reg = dff.groupby("Region")["Sales"].sum().reset_index()
col2.plotly_chart(px.pie(reg, names="Region", values="Sales", title="🗺️ Sales by Region", hole=0.4), use_container_width=True)

# ===== CHART 4: Top Products =====
top = dff.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index().sort_values("Sales")
st.plotly_chart(px.bar(top, x="Sales", y="Product Name", title="🏆 Top 10 Products"), use_container_width=True)

st.caption(f"Showing {len(dff):,} records")
