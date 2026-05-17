# ==============================================================================
#                      DATA ANALYTICS PORTFOLIO PROJECT
#           Sales & Financial Customer Analysis Using Python (Pandas)
# ==============================================================================
# This project demonstrates advanced data cleaning, multi-table relational merges,
# database connectivity pipelines, and strategic business data aggregations.
# ==============================================================================

import pandas as pd
import numpy as np

# ------------------------------------------------------------------------------
# SECTION 1: END-TO-END TRANSACTIONAL SALES ANALYSIS
# ------------------------------------------------------------------------------
print("=== SECTION 1: Executing Retail Sales Analysis ===")

raw_sales_data = [
    ['O001','2023-01-05','C001','Aisha','Mumbai','Laptop','Electronics',1,50000,50000],
    ['O002','2023-01-07','C002','Rahul','Delhi','Mobile','Electronics',2,20000,40000],
    ['O003','2023-01-10','C003','Meena','Chennai','Chair','Furniture',4,3000,12000],
    ['O004','2023-01-12','C001','Aisha','Mumbai','Headphones','Electronics',3,2000,6000],
    ['O005','2023-02-02','C004','Arjun','Bangalore','Table','Furniture',2,7000,14000],
    ['O006','2023-02-05','C005','Priya','Hyderabad','Sofa','Furniture',1,25000,25000],
    ['O007','2023-02-10','C002','Rahul','Delhi','Laptop','Electronics',1,52000,52000],
    ['O008','2023-02-15','C006','Kiran','Pune','Mobile','Electronics',1,18000,18000],
    ['O009','2023-03-01','C007','Sneha','Kolkata','Fan','Appliances',3,2500,7500],
    ['O010','2023-03-05','C003','Meena','Chennai','Desk','Furniture',1,8000,8000],
    ['O011','2023-03-10','C008','Vikram','Mumbai','AC','Appliances',1,35000,35000],
    ['O012','2023-03-15','C004','Arjun','Bangalore','Mobile','Electronics',2,22000,44000],
    ['O013','2023-04-01','C009','Anjali','Delhi','Washing Machine','Appliances',1,30000,30000],
    ['O014','2023-04-05','C010','Rohit','Hyderabad','Laptop','Electronics',1,48000,48000],
    ['O015','2023-04-10','C006','Kiran','Pune','Chair','Furniture',6,2800,16800],
    ['O016','2023-04-15','C005','Priya','Hyderabad','Mobile','Electronics',1,21000,21000],
    ['O017','2023-05-02','C001','Aisha','Mumbai','Sofa','Furniture',1,26000,26000],
    ['O018','2023-05-06','C007','Sneha','Kolkata','AC','Appliances',1,34000,34000],
    ['O019','2023-05-10','C002','Rahul','Delhi','Table','Furniture',1,7500,7500],
    ['O020','2023-05-15','C010','Rohit','Hyderabad','Headphones','Electronics',2,2500,5000]
]

columns_header = ['order_id','order_date','customer_id','customer_name',
                  'city','product','category','quantity','price','total_amount']

df_sales = pd.DataFrame(raw_sales_data, columns=columns_header)

# Data Standardization
df_sales = df_sales.drop_duplicates()
df_sales["order_date"] = pd.to_datetime(df_sales["order_date"])
df_sales["month"] = df_sales["order_date"].dt.month_name()

# Key Performance Indicator Calculations
total_revenue = df_sales["total_amount"].sum()
unique_customers = df_sales["customer_id"].nunique()
avg_order_value = df_sales['total_amount'].mean()

print(f"-> Total Revenue Generated: INR {total_revenue:,}")
print(f"-> Total Unique Customers Served: {unique_customers}")
print(f"-> Average Transaction Value: INR {avg_order_value:.2f}\n")

# ------------------------------------------------------------------------------
# SECTION 2: RELATIONAL ENTERPRISE BANKING PIPELINE (DATA MERGING)
# ------------------------------------------------------------------------------
print("=== SECTION 2: Enterprise Banking & Credit Analysis ===")

# Production mockup tables to simulate relational matching
mock_customer = pd.DataFrame({
    'customer_id': ['C001', 'C002', 'C003', 'C004'],
    'customer_name': ['Aisha', 'Rahul', 'Meena', 'Arjun'],
    'city': ['Mumbai', 'Delhi', 'Chennai', 'Bangalore'],
    'age': [28, 48, 35, 62],
    'gender': ['Female', 'Male', 'Female', 'Male'],
    'join_date': ['2021-06-15', '2020-01-10', '2022-03-22', '2019-11-05']
})

mock_transactions = pd.DataFrame({
    'transaction_id': ['T101', 'T102', 'T103', 'T104', 'T105'],
    'customer_id': ['C001', 'C002', 'C001', 'C003', 'C004'],
    'amount': [15000, 45000, 2500, 8000, 95000],
    'transaction_type': ['Debit', 'Debit', 'Credit', 'Debit', 'Debit'],
    'transaction_date': ['2023-10-01', '2023-11-15', '2023-12-05', '2023-08-20', '2023-05-12']
})

mock_loan = pd.DataFrame({
    'loan_id': ['L501', 'L502', 'L503', 'L504'],
    'customer_id': ['C001', 'C002', 'C003', 'C004'],
    'loan_amount': [500000, 1200000, 0, 350000]
})

# Combining tables using multi-key merges
df_banking = mock_customer.merge(mock_transactions, on="customer_id").merge(mock_loan, on="customer_id")
df_banking['transaction_date'] = pd.to_datetime(df_banking["transaction_date"])

# Custom Segment Binning (Fixed logical hierarchy constraint)
df_banking["age_group"] = df_banking["age"].apply(
    lambda x: "Younger (20-30)" if x <= 30 
    else "Middle Age (31-45)" if x <= 45 
    else "Senior (46+)"
)

print("--- Age-Group Distribution Metrics ---")
print(df_banking[['customer_name', 'age', 'age_group']])

# ------------------------------------------------------------------------------
# SECTION 3: EXECUTIVE SUMMARY MATRICES
# ------------------------------------------------------------------------------
print("\n=== SECTION 3: Executive Operational Performance Matrix ===")

executive_summary = df_sales.groupby("city").agg(
    total_revenue_generated=("total_amount", "sum"),
    average_order_value=("total_amount", "mean"),
    total_units_sold=("quantity", "sum"),
    total_order_frequency=("order_id", "count")
).sort_values(by="total_revenue_generated", ascending=False)

print(executive_summary)
print("\n==============================================================================")
