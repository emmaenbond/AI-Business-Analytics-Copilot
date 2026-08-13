# AI Business Analytics Copilot
Live Demo: https://emmaenbond-ai-business-analytics-copilot-dashboard-yfqnzd.streamlit.app/
An interactive business analytics dashboard built with Python, Pandas, Streamlit, and Matplotlib.

The application analyzes sales data, calculates key business metrics, creates visualizations, filters results by region, and allows users to ask common business questions through an analytics copilot interface.

## Features

* Interactive Streamlit web dashboard
* Analyze 1,000 sales transactions
* Region-based filtering
* Total sales calculation
* Total profit calculation
* Total order tracking
* Profit margin calculation
* Sales by category visualization
* Profit by category visualization
* Interactive sales data table
* Business-question interface
* Dynamic answers based on selected region

## Example Questions

The Analytics Copilot can answer questions such as:

* Which category has the highest sales?
* Which category has the highest profit?
* Which region has the highest sales?
* Which region has the highest profit?
* What are the total sales?
* What is the total profit?
* How many total orders are there?

## Technologies Used

* Python
* Pandas
* Streamlit
* Matplotlib
* CSV data processing
* VS Code

## Project Structure

```text
AI-Business-Analytics-Copilot/
│
├── app.py
├── dashboard.py
├── README.md
│
└── data/
    └── sales_data.csv
```

## Running the Project

Install the required Python libraries:

```bash
pip install pandas matplotlib streamlit
```

Run the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

Then open the local Streamlit address in your browser.

## How It Works

The application loads sales data from a CSV file using Pandas.

The dashboard calculates business KPIs and groups the data by categories and regions to identify sales and profit trends.

Users can select a region from the sidebar to dynamically update the dashboard.

The Analytics Copilot accepts business questions and uses the filtered dataset to return relevant answers.

## Key Business Metrics

The dashboard displays:

* Total Sales
* Total Profit
* Total Orders
* Profit Margin

All metrics automatically update when a different region is selected.

## Purpose

This project demonstrates practical experience with:

* Python programming
* Data analysis
* Data visualization
* Business intelligence
* Interactive dashboard development
* Data filtering and aggregation
* User-driven analytics

## Future Improvements

Potential future enhancements include:

* Integration with an LLM API for more advanced natural-language questions
* Database integration
* Date-range filtering
* Product-level filtering
* Sales forecasting
* Automated business insights
* Cloud deployment
