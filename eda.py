import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------
# 1. Create the dataset
# -----------------------------------

data = {
    "Product_ID": [
        "P001", "P002", "P003", "P004", "P005",
        "P006", "P007", "P008", "P009", "P010"
    ],

    "Product": [
        "Milk", "Milk", "Milk", "Milk", "Milk",
        "Milk", "Yogurt", "Yogurt", "Yogurt", "Yogurt"
    ],

    "Manufacture_Date": [
        "2026-01-01", "2026-01-02", "2026-01-03",
        "2026-01-04", "2026-01-05", "2026-01-06",
        "2026-01-01", "2026-01-05", "2026-01-10",
        "2026-01-13"
    ],

    "Expiry_Date": [
        "2026-01-07", "2026-01-07", "2026-01-07",
        "2026-01-07", "2026-01-07", "2026-01-07",
        "2026-01-15", "2026-01-15", "2026-01-15",
        "2026-01-15"
    ],

    "Days_To_Expiry": [6, 5, 4, 3, 2, 1, 14, 10, 5, 2],

    "Price": [50, 50, 50, 50, 50, 50, 80, 80, 80, 80],

    "Discount": [0, 0, 5, 10, 20, 30, 0, 5, 15, 25],

    "Stock": [100, 90, 85, 70, 60, 50, 100, 90, 70, 60],

    "Sales_Units": [80, 65, 52, 40, 25, 10, 75, 65, 38, 18],

    "Customer_Demand": [
        "High", "High", "Medium", "Medium", "Low",
        "Low", "High", "High", "Medium", "Low"
    ],

    "Sales_Level": [
        "High", "High", "Medium", "Medium", "Low",
        "Low", "High", "High", "Medium", "Low"
    ]
}

df = pd.DataFrame(data)


# -----------------------------------
# 2. Display the dataset
# -----------------------------------

print("\nDATASET:")
print(df)


# -----------------------------------
# 3. First 5 rows
# -----------------------------------

print("\nFIRST 5 ROWS:")
print(df.head())


# -----------------------------------
# 4. Dataset information
# -----------------------------------

print("\nDATASET INFORMATION:")
print(df.info())


# -----------------------------------
# 5. Statistical summary
# -----------------------------------

print("\nSTATISTICAL SUMMARY:")
print(df.describe())


# -----------------------------------
# 6. Check missing values
# -----------------------------------

print("\nMISSING VALUES:")
print(df.isnull().sum())


# -----------------------------------
# 7. Check duplicate values
# -----------------------------------

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())


# -----------------------------------
# 8. Convert dates
# -----------------------------------

df["Manufacture_Date"] = pd.to_datetime(df["Manufacture_Date"])
df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"])


# -----------------------------------
# 9. Average sales
# -----------------------------------

print("\nAVERAGE SALES:")
print(df["Sales_Units"].mean())


# -----------------------------------
# 10. Total sales
# -----------------------------------

print("\nTOTAL SALES:")
print(df["Sales_Units"].sum())


# -----------------------------------
# 11. Sales by product
# -----------------------------------

print("\nSALES BY PRODUCT:")
print(df.groupby("Product")["Sales_Units"].sum())


# -----------------------------------
# 12. Average sales by customer demand
# -----------------------------------

print("\nAVERAGE SALES BY CUSTOMER DEMAND:")
print(df.groupby("Customer_Demand")["Sales_Units"].mean())


# -----------------------------------
# 13. Correlation
# -----------------------------------

print("\nCORRELATION:")
print(
    df[
        [
            "Days_To_Expiry",
            "Price",
            "Discount",
            "Stock",
            "Sales_Units"
        ]
    ].corr()
)


# -----------------------------------
# 14. Visualization
# -----------------------------------

sns.set_style("whitegrid")


# Days to expiry vs sales
plt.figure(figsize=(8, 5))

sns.scatterplot(
    x="Days_To_Expiry",
    y="Sales_Units",
    hue="Product",
    data=df,
    s=100
)

plt.title("Days to Expiry vs Sales")
plt.xlabel("Days to Expiry")
plt.ylabel("Sales Units")

plt.show()


# -----------------------------------
# 15. Discount vs sales
# -----------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x="Discount",
    y="Sales_Units",
    hue="Product",
    data=df,
    s=100
)

plt.title("Discount vs Sales")
plt.xlabel("Discount (%)")
plt.ylabel("Sales Units")

plt.show()


# -----------------------------------
# 16. Stock vs sales
# -----------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x="Stock",
    y="Sales_Units",
    hue="Product",
    data=df,
    s=100
)

plt.title("Stock vs Sales")
plt.xlabel("Stock")
plt.ylabel("Sales Units")

plt.show()


# -----------------------------------
# 17. Sales by product
# -----------------------------------

plt.figure(figsize=(7, 5))

sns.barplot(
    x="Product",
    y="Sales_Units",
    data=df
)

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales Units")

plt.show()


# -----------------------------------
# 18. Sales level count
# -----------------------------------

plt.figure(figsize=(7, 5))

sns.countplot(
    x="Sales_Level",
    data=df
)

plt.title("Sales Level Distribution")
plt.xlabel("Sales Level")
plt.ylabel("Number of Products")

plt.show()


# -----------------------------------
# 19. Correlation heatmap
# -----------------------------------

plt.figure(figsize=(8, 6))

correlation = df[
    [
        "Days_To_Expiry",
        "Price",
        "Discount",
        "Stock",
        "Sales_Units"
    ]
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()
