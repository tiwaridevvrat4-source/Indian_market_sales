# Indian Market Sales Analysis

## Live Dashboard

**Explore the Interactive Streamlit Dashboard:**
[Indian Market Sales Analysis – Live Dashboard](https://indianmarketsales-devvrat.streamlit.app/?utm_source=chatgpt.com)

---

## Project Overview

Indian Market Sales Analysis is an Exploratory Data Analysis (EDA) project developed using Python, Pandas, Matplotlib, Seaborn, and Streamlit.

The project analyses Indian market sales data to understand sales performance, product categories, regional performance, payment methods, units sold, delivery patterns, holiday impact, and time-based sales trends.

An interactive Streamlit dashboard has been developed to present the analysis in a clean and user-friendly format.

## Dataset

The dataset contains **200 sales records** with the following original columns:

* SaleID
* OrderDate
* DeliveryDate
* ProductCategory
* Region
* SalesAmount
* UnitsSold
* PaymentMethod
* IsHoliday

Additional analytical features were created:

* Total sales
* DeliveryDays
* Year
* Month
* MonthName
* dayName

## Analysis Performed

### Univariate Analysis

The distribution of numerical variables was analysed using:

* Histograms
* KDE plots
* Boxplots
* Descriptive statistics

Variables include:

* SalesAmount
* UnitsSold
* Total sales
* DeliveryDays

### Bivariate Analysis

Relationships and comparisons were explored using:

* Scatter plots
* Correlation analysis
* Monthly comparisons
* Day-wise comparisons

### Multivariate Analysis

The project also analyses multiple business dimensions together:

* Region vs Product Category
* Region vs Payment Method
* Month vs Product Category
* Holiday vs Total Sales
* Correlation Heatmap

## Dashboard Sections

### Home

Provides:

* Project overview
* Dataset summary
* Key business metrics
* Dataset preview
* Column guide

### EDA Analysis

Provides interactive:

* Univariate Analysis
* Bivariate Analysis
* Monthly Comparison
* Day-wise Comparison
* Multivariate Analysis
* Correlation Heatmap

### Conclusion & Insights

Summarizes the major findings and business insights obtained from the complete analysis.

## Key Metrics

The dashboard includes:

* Total Orders
* Total Sales
* Total Units Sold
* Average Delivery Days

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit

## Project Structure

```text
Indian_Market/
│
├── Home.py
├── indian_market.csv
├── requirements.txt
│
└── pages/
    ├── 1_EDA_Analysis.py
    └── 2_Conclusion_Insights.py
```

## Objective

The objective of this project is to transform raw Indian market sales data into meaningful business insights using Python-based Exploratory Data Analysis and an interactive Streamlit dashboard.

This project demonstrates practical skills in:

* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis
* Data Visualization
* Business Analytics
* Python
* Streamlit Dashboard Development

## Project Links

**Live Dashboard:**
[Indian Market Sales Analysis](https://indianmarketsales-devvrat.streamlit.app/?utm_source=chatgpt.com)

**GitHub Repository:**
[View Source Code on GitHub](https://github.com/tiwaridevvrat4-source/indian-market-sales?utm_source=chatgpt.com)
