import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="EDA Analysis",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("indian_market.csv")

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

st.sidebar.subheader("EDA Analysis")

analysis_type = st.sidebar.radio(
    "Analysis Type",
    [
        "Univariate Analysis",
        "Bivariate Analysis",
        "Multivariate Analysis"
    ]
)

st.sidebar.divider()

st.sidebar.caption(
    "Indian Market Sales Analysis"
)


# =========================
# MAIN
# =========================

st.title("Exploratory Data Analysis")

st.write(
    "Explore sales performance, product categories, "
    "regions, payment methods and delivery patterns."
)

st.divider()


# =====================================================
# UNIVARIATE
# =====================================================

if analysis_type == "Univariate Analysis":

    st.header("Univariate Analysis")

    st.caption(
        "Understand the distribution of individual numerical variables."
    )

    numerical_columns = [
        "SalesAmount",
        "UnitsSold",
        "Total sales",
        "DeliveryDays"
    ]

    column = st.selectbox(
        "Select Variable",
        numerical_columns
    )

    data = pd.to_numeric(
        df[column],
        errors="coerce"
    ).dropna()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Count",
            f"{len(data):,}"
        )

    with col2:
        st.metric(
            "Mean",
            f"{data.mean():,.2f}"
        )

    with col3:
        st.metric(
            "Minimum",
            f"{data.min():,.2f}"
        )

    with col4:
        st.metric(
            "Maximum",
            f"{data.max():,.2f}"
        )

    st.divider()

    st.subheader("Distribution")

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    sns.histplot(
        data,
        bins=30,
        kde=True,
        ax=ax
    )

    ax.set_title(
        f"Distribution of {column}"
    )

    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

    st.pyplot(fig)

    st.subheader("Boxplot")

    fig, ax = plt.subplots(
        figsize=(10, 3)
    )

    sns.boxplot(
        x=data,
        ax=ax
    )

    ax.set_title(
        f"Distribution of {column}"
    )

    st.pyplot(fig)

    st.subheader("Detailed Statistics")

    st.dataframe(
        data.describe().to_frame("Value"),
        use_container_width=True
    )


# =====================================================
# BIVARIATE
# =====================================================

elif analysis_type == "Bivariate Analysis":

    st.header("Bivariate Analysis")

    st.caption(
        "Compare numerical variables and analyse sales patterns "
        "across months and days."
    )

    # --------------------------------------------------
    # NUMERICAL COMPARISON
    # --------------------------------------------------

    st.subheader("Numerical Variable Comparison")

    numerical_columns = [
        "SalesAmount",
        "UnitsSold",
        "Total sales",
        "DeliveryDays"
    ]

    col1, col2 = st.columns(2)

    with col1:
        x = st.selectbox(
            "X Variable",
            numerical_columns,
            key="bivariate_x"
        )

    with col2:
        y = st.selectbox(
            "Y Variable",
            numerical_columns,
            index=1,
            key="bivariate_y"
        )

    plot_df = df[[x, y]].copy()

    plot_df[x] = pd.to_numeric(
        plot_df[x],
        errors="coerce"
    )

    plot_df[y] = pd.to_numeric(
        plot_df[y],
        errors="coerce"
    )

    plot_df = plot_df.dropna()

    correlation = plot_df[x].corr(plot_df[y])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Correlation",
            f"{correlation:.3f}"
        )

    with col2:
        st.metric(
            "Observations",
            f"{len(plot_df):,}"
        )

    with col3:
        st.metric(
            "Average " + y,
            f"{plot_df[y].mean():,.2f}"
        )

    st.divider()

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.scatterplot(
        data=plot_df,
        x=x,
        y=y,
        ax=ax
    )

    ax.set_title(f"{x} vs {y}")
    ax.set_xlabel(x)
    ax.set_ylabel(y)

    st.pyplot(fig)

    st.divider()


    # --------------------------------------------------
    # MONTH COMPARISON
    # --------------------------------------------------

    st.subheader("Monthly Comparison")

    month_metric = st.selectbox(
        "Select Metric for Month Comparison",
        [
            "Total sales",
            "SalesAmount",
            "UnitsSold",
            "DeliveryDays"
        ],
        key="month_metric"
    )

    monthly_data = (
        df.groupby("Month")[month_metric]
        .agg(["sum", "mean"])
        .reset_index()
    )

    monthly_data["MonthName"] = pd.to_datetime(
        monthly_data["Month"],
        format="%m"
    ).dt.month_name().str[:3]

    monthly_data = monthly_data.sort_values("Month")

    fig, ax = plt.subplots(figsize=(12, 5))

    sns.barplot(
        data=monthly_data,
        x="MonthName",
        y="sum",
        ax=ax
    )

    ax.set_title(
        f"Monthly {month_metric} Comparison"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel(
        f"Total {month_metric}"
    )

    st.pyplot(fig)

    st.write("Monthly Summary")

    monthly_display = monthly_data[
        ["MonthName", "sum", "mean"]
    ].copy()

    monthly_display.columns = [
        "Month",
        "Total",
        "Average"
    ]

    st.dataframe(
        monthly_display,
        use_container_width=True
    )

    st.divider()


    # --------------------------------------------------
    # DAY COMPARISON
    # --------------------------------------------------

    st.subheader("Day-wise Comparison")

    day_metric = st.selectbox(
        "Select Metric for Day Comparison",
        [
            "Total sales",
            "SalesAmount",
            "UnitsSold",
            "DeliveryDays"
        ],
        key="day_metric"
    )

    day_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    daily_data = (
        df.groupby("dayName")[day_metric]
        .agg(["sum", "mean"])
        .reindex(day_order)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12, 5))

    sns.barplot(
        data=daily_data,
        x="dayName",
        y="sum",
        ax=ax
    )

    ax.set_title(
        f"Day-wise {day_metric} Comparison"
    )

    ax.set_xlabel("Day")
    ax.set_ylabel(
        f"Total {day_metric}"
    )

    plt.xticks(rotation=30)

    st.pyplot(fig)

    st.write("Day-wise Summary")

    daily_display = daily_data[
        ["dayName", "sum", "mean"]
    ].copy()

    daily_display.columns = [
        "Day",
        "Total",
        "Average"
    ]

    st.dataframe(
        daily_display,
        use_container_width=True
    )


# =====================================================
# MULTIVARIATE
# =====================================================

else:

    st.header("Multivariate Analysis")

    st.caption(
        "Analyze multiple sales dimensions together."
    )

    # -------------------------
    # Region + Category
    # -------------------------

    st.subheader(
        "Total Sales by Region and Product Category"
    )

    region_category = (
        df.groupby(
            ["Region", "ProductCategory"]
        )["Total sales"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(
        figsize=(12, 6)
    )

    sns.barplot(
        data=region_category,
        x="Region",
        y="Total sales",
        hue="ProductCategory",
        ax=ax
    )

    ax.set_title(
        "Total Sales by Region and Product Category"
    )

    ax.set_xlabel("Region")
    ax.set_ylabel("Total Sales")

    plt.xticks(rotation=30)

    st.pyplot(fig)

    st.divider()

    # -------------------------
    # Payment + Region
    # -------------------------

    st.subheader(
        "Total Sales by Region and Payment Method"
    )

    payment_region = (
        df.groupby(
            ["Region", "PaymentMethod"]
        )["Total sales"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(
        figsize=(12, 6)
    )

    sns.barplot(
        data=payment_region,
        x="Region",
        y="Total sales",
        hue="PaymentMethod",
        ax=ax
    )

    ax.set_title(
        "Total Sales by Region and Payment Method"
    )

    ax.set_xlabel("Region")
    ax.set_ylabel("Total Sales")

    plt.xticks(rotation=30)

    st.pyplot(fig)

    st.divider()

    # -------------------------
    # Monthly Category
    # -------------------------

    st.subheader(
        "Monthly Total Sales by Product Category"
    )

    monthly_category = (
        df.groupby(
            ["Month", "ProductCategory"]
        )["Total sales"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(
        figsize=(14, 6)
    )

    sns.barplot(
        data=monthly_category,
        x="Month",
        y="Total sales",
        hue="ProductCategory",
        ax=ax
    )

    ax.set_title(
        "Monthly Total Sales by Product Category"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Total Sales")

    st.pyplot(fig)

    st.divider()

    # -------------------------
    # Correlation Heatmap
    # -------------------------

    st.subheader(
        "Correlation Heatmap"
    )

    numeric_columns = [
        "SalesAmount",
        "UnitsSold",
        "Total sales",
        "DeliveryDays"
    ]

    correlation_data = df[
        numeric_columns
    ].corr()

    fig, ax = plt.subplots(
        figsize=(8, 6)
    )

    sns.heatmap(
        correlation_data,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        ax=ax
    )

    ax.set_title(
        "Correlation Heatmap"
    )

    st.pyplot(fig)

    st.divider()

    # -------------------------
    # Holiday Analysis
    # -------------------------

    st.subheader(
        "Total Sales by Holiday Status"
    )

    holiday_sales = (
        df.groupby("IsHoliday")["Total sales"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    sns.barplot(
        data=holiday_sales,
        x="IsHoliday",
        y="Total sales",
        ax=ax
    )

    ax.set_title(
        "Total Sales by Holiday Status"
    )

    ax.set_xlabel("Holiday")
    ax.set_ylabel("Total Sales")

    st.pyplot(fig)