import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Conclusion & Insights",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("indian_market.csv")

# Date conversion
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
df["DeliveryDate"] = pd.to_datetime(df["DeliveryDate"], errors="coerce")

# Derived columns
df["Total sales"] = df["SalesAmount"] * df["UnitsSold"]
df["DeliveryDays"] = (
    df["DeliveryDate"] - df["OrderDate"]
).dt.days

df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.month
df["MonthName"] = df["OrderDate"].dt.month_name()
df["dayName"] = df["OrderDate"].dt.day_name()


# --------------------------------------------------
# SALES FORMATTER
# --------------------------------------------------

def format_sales(value):

    if value >= 1_00_00_000:
        return f"₹{value / 1_00_00_000:.2f} Cr"

    elif value >= 1_00_000:
        return f"₹{value / 1_00_000:.2f} L"

    elif value >= 1_000:
        return f"₹{value / 1_000:.1f} K"

    else:
        return f"₹{value:.0f}"


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("Indian Market Analysis")

st.sidebar.divider()

st.sidebar.subheader("Conclusion & Insights")

st.sidebar.write(
    "Explore the major findings, sales patterns, "
    "delivery performance and business insights."
)

st.sidebar.divider()

st.sidebar.caption("Indian Market Sales Analysis")


# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------

st.title("Conclusion & Insights")

st.write(
    "Key findings and business insights derived from "
    "the Indian Market Sales Analysis."
)

st.divider()


# --------------------------------------------------
# KEY BUSINESS METRICS
# --------------------------------------------------

st.header("Key Business Metrics")

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
        format_sales(total_sales)
    )

with col3:
    st.metric(
        "Total Units Sold",
        f"{total_units:,}"
    )

with col4:
    st.metric(
        "Avg. Delivery",
        f"{avg_delivery:.1f} Days"
    )


st.divider()


# --------------------------------------------------
# DATA QUALITY
# --------------------------------------------------

st.header("Data Quality Findings")

missing_values = df.isnull().sum().sum()
duplicate_rows = df.duplicated().sum()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Records",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "Missing Values",
        f"{missing_values:,}"
    )

with col3:
    st.metric(
        "Duplicate Rows",
        f"{duplicate_rows:,}"
    )

st.write(
    "The dataset contains 200 records across 9 original columns. "
    "The analysis also uses derived variables such as Total sales, "
    "DeliveryDays, Year, Month, MonthName and dayName."
)


st.divider()


# --------------------------------------------------
# SALES INSIGHTS
# --------------------------------------------------

st.header("Sales Insights")

top_category = (
    df.groupby("ProductCategory")["Total sales"]
    .sum()
    .sort_values(ascending=False)
)

top_region = (
    df.groupby("Region")["Total sales"]
    .sum()
    .sort_values(ascending=False)
)

top_payment = (
    df.groupby("PaymentMethod")["Total sales"]
    .sum()
    .sort_values(ascending=False)
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Top Product Category")

    st.write(
        f"**{top_category.index[0]}**"
    )

    st.caption(
        f"Sales: {format_sales(top_category.iloc[0])}"
    )

with col2:
    st.subheader("Top Region")

    st.write(
        f"**{top_region.index[0]}**"
    )

    st.caption(
        f"Sales: {format_sales(top_region.iloc[0])}"
    )

with col3:
    st.subheader("Top Payment Method")

    st.write(
        f"**{top_payment.index[0]}**"
    )

    st.caption(
        f"Sales: {format_sales(top_payment.iloc[0])}"
    )


st.divider()


# --------------------------------------------------
# DELIVERY INSIGHTS
# --------------------------------------------------

st.header("Delivery Insights")

fastest_delivery = df["DeliveryDays"].min()
slowest_delivery = df["DeliveryDays"].max()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Delivery",
        f"{avg_delivery:.1f} Days"
    )

with col2:
    st.metric(
        "Fastest Delivery",
        f"{fastest_delivery} Days"
    )

with col3:
    st.metric(
        "Longest Delivery",
        f"{slowest_delivery} Days"
    )

st.write(
    "DeliveryDays was derived from the difference between "
    "DeliveryDate and OrderDate. The average value provides "
    "an overall view of delivery performance."
)


st.divider()


# --------------------------------------------------
# UNITS SOLD INSIGHTS
# --------------------------------------------------

st.header("Units Sold Insights")

total_units = df["UnitsSold"].sum()
average_units = df["UnitsSold"].mean()
maximum_units = df["UnitsSold"].max()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Units",
        f"{total_units:,}"
    )

with col2:
    st.metric(
        "Average Units / Order",
        f"{average_units:.1f}"
    )

with col3:
    st.metric(
        "Maximum Units / Order",
        f"{maximum_units:,}"
    )


st.write(
    "UnitsSold helps evaluate the quantity of products sold "
    "across individual orders and the dataset as a whole."
)


st.divider()


# --------------------------------------------------
# HOLIDAY ANALYSIS
# --------------------------------------------------

st.header("Holiday Sales Analysis")

holiday_sales = (
    df.groupby("IsHoliday")["Total sales"]
    .sum()
    .sort_values(ascending=False)
)

holiday_orders = (
    df.groupby("IsHoliday")
    .size()
    .sort_values(ascending=False)
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("Sales by Holiday Status")

    for status, value in holiday_sales.items():

        status_text = "Holiday" if status else "Non-Holiday"

        st.write(
            f"**{status_text}** — {format_sales(value)}"
        )

with col2:

    st.subheader("Orders by Holiday Status")

    for status, value in holiday_orders.items():

        status_text = "Holiday" if status else "Non-Holiday"

        st.write(
            f"**{status_text}** — {value:,} orders"
        )


st.divider()


# --------------------------------------------------
# TIME BASED INSIGHTS
# --------------------------------------------------

st.header("Time-Based Insights")

monthly_sales = (
    df.groupby("MonthName")["Total sales"]
    .sum()
    .sort_values(ascending=False)
)

daily_sales = (
    df.groupby("dayName")["Total sales"]
    .sum()
    .sort_values(ascending=False)
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("Top Sales Month")

    st.write(
        f"**{monthly_sales.index[0]}**"
    )

    st.caption(
        f"Sales: {format_sales(monthly_sales.iloc[0])}"
    )

with col2:

    st.subheader("Top Sales Day")

    st.write(
        f"**{daily_sales.index[0]}**"
    )

    st.caption(
        f"Sales: {format_sales(daily_sales.iloc[0])}"
    )


st.divider()


# --------------------------------------------------
# MAJOR OBSERVATIONS
# --------------------------------------------------

st.header("Major Observations")

st.markdown(
    f"""
- The dataset contains **{total_orders:,} orders**.
- Total sales generated from the analysis are **{format_sales(total_sales)}**.
- **{top_category.index[0]}** is the highest-selling product category based on total sales.
- **{top_region.index[0]}** generates the highest total sales among the analysed regions.
- **{top_payment.index[0]}** is the leading payment method based on total sales.
- The average delivery time is approximately **{avg_delivery:.1f} days**.
- Time-based analysis shows that sales vary across different months and days.
- Holiday and non-holiday sales can be compared to understand differences in purchasing activity.
"""
)


st.divider()


# --------------------------------------------------
# OVERALL CONCLUSION
# --------------------------------------------------

st.header("Overall Conclusion")

st.write(
    "The Indian Market Sales Analysis provides a structured view "
    "of sales performance across products, regions, payment methods, "
    "delivery time and calendar-based factors."
)

st.write(
    "The analysis combines the original sales variables with derived "
    "metrics such as Total sales and DeliveryDays to identify important "
    "patterns in the dataset."
)

st.write(
    "The EDA demonstrates how sales data can be transformed into "
    "business-oriented insights that help understand product demand, "
    "regional performance, payment preferences and delivery behaviour."
)


st.divider()


# --------------------------------------------------
# FINAL SUMMARY
# --------------------------------------------------

st.header("Final Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Sales")

    st.write(
        f"Total sales: **{format_sales(total_sales)}**"
    )

with col2:
    st.subheader("Orders")

    st.write(
        f"Total orders: **{total_orders:,}**"
    )

with col3:
    st.subheader("Delivery")

    st.write(
        f"Average: **{avg_delivery:.1f} days**"
    )