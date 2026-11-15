import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Sales Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("sales_data.csv")

# Standardize column names
df.columns = df.columns.str.lower()

# Dashboard Title
st.title("📊 Sales Data Analysis Dashboard")
st.subheader("Sales Performance Overview")

# Show Dataset
st.write("### Sales Dataset")
st.dataframe(df)

# SALES SUMMARY CARDS

st.write("## 📈 Sales Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Revenue",
    f"Rs. {df['total_sales'].sum():,}"
)

col2.metric(
    "Total Products",
    df["product"].nunique()
)

col3.metric(
    "Quantity Sold",
    df["quantity"].sum()
)

col4.metric(
    "Sales Records",
    len(df)
)

# PRODUCT WISE SALES GRAPH

st.write("## 📊 Product Wise Sales")

product_sales = df.groupby("product")["quantity"].sum()

st.bar_chart(product_sales)


# CATEGORY WISE REVENUE GRAPH

st.write("## 💰 Category Wise Revenue")

category_sales = df.groupby("category")["total_sales"].sum()

st.bar_chart(category_sales)


# DAILY SALES TREND

st.write("## 📅 Daily Sales Trend")

df["date"] = pd.to_datetime(df["date"])

daily_sales = df.groupby("date")["total_sales"].sum()

st.line_chart(daily_sales)

# PRODUCT SEARCH

st.write("## 🔍 Search Product")

selected_product = st.selectbox(
    "Select a Product",
    ["All Products"] + sorted(df["product"].unique().tolist())
)

if selected_product == "All Products":
    filtered_df = df
else:
    filtered_df = df[df["product"] == selected_product]

st.write("### Product Details")
st.dataframe(filtered_df)

st.write(
    "Total Revenue: Rs.",
    filtered_df["total_sales"].sum()
)