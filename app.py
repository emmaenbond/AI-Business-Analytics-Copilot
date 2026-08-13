import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/sales_data.csv")

print("AI Business Analytics Copilot")
print("-----------------------------")

print(f"Total Sales: ${df['Sales'].sum():,.2f}")
print(f"Total Profit: ${df['Profit'].sum():,.2f}")
print(f"Total Orders: {len(df)}")

print()
print("Sales by Region:")
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(region_sales)

best_region = region_sales.idxmax()
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
best_category = category_sales.idxmax()
product_sales = df.groupby("Product_Name")["Sales"].sum().sort_values(ascending=False)
best_product = product_sales.idxmax()
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
best_profit_category = category_profit.idxmax()

region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
best_profit_region = region_profit.idxmax()
print()
print("Highest Sales Region:", best_region)
print()
question = input("Ask your business question: ")
q = question.lower()

if "category" in q and "profit" in q and ("highest" in q or "best" in q or "top" in q):
    print(f"Answer: {best_profit_category} has the highest profit.")

elif "region" in q and "profit" in q and ("highest" in q or "best" in q or "top" in q):
    print(f"Answer: {best_profit_region} has the highest profit.")

elif "region" in q and ("highest" in q or "best" in q or "top" in q):
    print(f"Answer: {best_region} has the highest sales.")

elif "category" in q and ("highest" in q or "best" in q or "top" in q):
    print(f"Answer: {best_category} has the highest sales.")

elif "product" in q and ("highest" in q or "best" in q or "top" in q):
    print(f"Answer: {best_product} has the highest sales.")

elif "total sales" in q:
    print(f"Answer: Total sales are ${df['Sales'].sum():,.2f}.")

elif "total profit" in q:
    print(f"Answer: Total profit is ${df['Profit'].sum():,.2f}.")

elif "total orders" in q:
    print(f"Answer: There are {len(df)} total orders.")
elif "compare" in q and "sales" in q and "profit" in q and "category" in q:
    category_summary = df.groupby("Category")[["Sales", "Profit"]].sum()
    print("Answer:")
    print(category_summary)
elif "sales" in q and "category" in q and ("chart" in q or "graph" in q or "show" in q):
    category_sales.plot(kind="bar")
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales ($)")
    plt.tight_layout()
    plt.show()
else:
    print("I don't know how to answer that question yet.")