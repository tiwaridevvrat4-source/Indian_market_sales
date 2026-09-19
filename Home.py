import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Indian Market Sales Analysis",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("indian_market.csv")

# Create derived columns if not already present
df["OrderDate"] = pd.to_datetime(
    df["OrderDate"],
    errors="coerce"
)

df["DeliveryDate"] = pd.to_datetime(
    df["DeliveryDate"],
    errors="coerce"
)

df["Total sales"] = (
    df["SalesAmount"] * df["UnitsSold"]
)

df["DeliveryDays"] = (
    df["DeliveryDate"] - df["OrderDate"]
).dt.days

df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.month
df["MonthName"] = df["OrderDate"].dt.month_name()
df["dayName"] = df["OrderDate"].dt.day_name()


# =========================
# SIDEBAR
# =========================

st.sidebar.title("Indian Market Analysis")
st.sidebar.divider()

st.sidebar.subheader("Dashboard")
st.sidebar.write(
    "Use the navigation menu to explore "
    "the Indian market sales analysis."
)

st.sidebar.divider()

st.sidebar.subheader("Project Information")
st.sidebar.write(
    "This dashboard presents an exploratory "
    "analysis of Indian market sales data."
)

st.sidebar.divider()

st.sidebar.caption(
    "Built with Python and Streamlit"
)


# =========================
# HOME
# =========================

st.title("Indian Market Sales Analysis")

st.write(
    "An interactive exploratory data analysis dashboard "
    "for understanding sales performance, product categories, "
    "regions, payment methods and delivery patterns."
)

st.divider()


# =========================
# PROJECT OVERVIEW
# =========================

st.header("Project Overview")

st.write(
    "This project analyzes Indian market sales data to "
    "identify important patterns related to sales, products, "
    "regions, payment methods, holidays and delivery time."
)

st.write(
    "The analysis includes data validation, feature engineering, "
    "Univariate Analysis, Bivariate Analysis and Multivariate Analysis."
)

st.divider()


# =========================
# DATASET SUMMARY
# =========================

st.header("Dataset Summary")

total_orders = len(df)
total_sales = df["Total sales"].sum()
total_units = df["UnitsSold"].sum()
avg_delivery = df["DeliveryDays"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Orders",
        f"{total_orders:,}"
    )

with col2:
    st.metric(
        "Total Sales",
        f"{total_sales:,.2f}"
    )

with col3:
    st.metric(
        "Total Units Sold",
        f"{total_units:,}"
    )

with col4:
    st.metric(
        "Average Delivery Days",
        f"{avg_delivery:.2f}"
    )


st.divider()


# =========================
# DATASET PREVIEW
# =========================

st.header("Dataset Preview")

with st.expander("View Dataset"):

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True
    )


st.divider()


# =========================
# ANALYSIS COVERED
# =========================

st.header("Analysis Covered")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Univariate Analysis")

    st.write(
        "Distribution analysis of Sales Amount, "
        "Units Sold, Total Sales and Delivery Days."
    )


with col2:

    st.subheader("Bivariate Analysis")

    st.write(
        "Relationships between Units Sold, "
        "Delivery Days and Total Sales."
    )


with col3:

    st.subheader("Multivariate Analysis")

    st.write(
        "Combined analysis of Region, Product Category, "
        "Payment Method, Month and Sales."
    )


st.divider()


# =========================
# COLUMN GUIDE
# =========================

st.header("Column Guide")

column_descriptions = {

    "OrderDate":
        "Date on which the order was placed.",

    "DeliveryDate":
        "Date on which the order was delivered.",

    "ProductCategory":
        "Category of the product sold.",

    "Region":
        "Region associated with the order.",

    "SalesAmount":
        "Sales amount generated from the order.",

    "UnitsSold":
        "Number of units sold.",

    "PaymentMethod":
        "Payment method used for the order.",

    "IsHoliday":
        "Indicates whether the order date was a holiday.",

    "Total sales":
        "Calculated as SalesAmount multiplied by UnitsSold.",

    "DeliveryDays":
        "Number of days between OrderDate and DeliveryDate.",

    "Year":
        "Year extracted from OrderDate.",

    "Month":
        "Numeric month extracted from OrderDate.",

    "MonthName":
        "Month name extracted from OrderDate.",

    "dayName":
        "Day name extracted from OrderDate."
}

feature_df = pd.DataFrame(
    list(column_descriptions.items()),
    columns=[
        "Column Name",
        "Description"
    ]
)

st.dataframe(
    feature_df,
    use_container_width=True,
    hide_index=True
)


st.divider()


# =========================
# DASHBOARD STRUCTURE
# =========================

st.header("Dashboard Structure")

st.write(
    "**Home:** Project introduction and dataset overview."
)

st.write(
    "**EDA Analysis:** Interactive Univariate, "
    "Bivariate and Multivariate analysis."
)

st.write(
    "**Conclusion & Insights:** Key observations "
    "and business insights from the analysis."
)