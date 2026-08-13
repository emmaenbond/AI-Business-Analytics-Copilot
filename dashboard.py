import streamlit as st
import pandas as pd

df = pd.read_csv("data/sales_data.csv")
st.sidebar.header("Filters")

regions = ["All"] + sorted(df["Region"].unique().tolist())

selected_region = st.sidebar.selectbox(
    "Select Region",
    regions
)

if selected_region == "All":
    filtered_df = df
else:
    filtered_df = df[df["Region"] == selected_region]
st.set_page_config(
    page_title="AI Business Analytics Copilot",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Business Analytics Copilot")
st.write("Interactive business intelligence dashboard")

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = len(filtered_df)
profit_margin = (total_profit / total_sales) * 100
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Profit Margin", f"{profit_margin:.1f}%")
st.subheader("Sales by Category")

category_sales = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_sales)
st.subheader("Profit by Category")

category_profit = (
    filtered_df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_profit)

st.subheader("Sales Data")
st.dataframe(filtered_df)
st.subheader("Ask the Analytics Copilot")

question = st.text_input(
    "Ask a business question:",
    placeholder="Example: Which category has the highest sales?"
)

if question:
    q = question.lower()

    if "category" in q and "profit" in q and ("highest" in q or "best" in q or "top" in q):
        result = filtered_df.groupby("Category")["Profit"].sum().idxmax()
        st.success(f"{result} has the highest profit.")

    elif "category" in q and ("highest" in q or "best" in q or "top" in q):
        result = filtered_df.groupby("Category")["Sales"].sum().idxmax()
        st.success(f"{result} has the highest sales.")

    elif "region" in q and "profit" in q and ("highest" in q or "best" in q or "top" in q):
        result = filtered_df.groupby("Region")["Profit"].sum().idxmax()
        st.success(f"{result} has the highest profit.")

    elif "region" in q and ("highest" in q or "best" in q or "top" in q):
        result = filtered_df.groupby("Region")["Sales"].sum().idxmax()
        st.success(f"{result} has the highest sales.")

    elif "total sales" in q:
        st.success(f"Total sales are ${filtered_df['Sales'].sum():,.2f}.")

    elif "total profit" in q:
        st.success(f"Total profit is ${filtered_df['Profit'].sum():,.2f}.")

    elif "total orders" in q:
        st.success(f"There are {len(filtered_df):,} total orders.")

    else:
        st.warning("I don't know how to answer that question yet.")