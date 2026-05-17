# Python-Sales-And-Customer-Analytics
A Pandas data wrangling portfolio script demonstrating multi-table relational merges, categorical group aggregations, and business KPI generation.
# Customer & Sales Data Analysis with Python (Pandas)

## Project Overview
This repository contains a comprehensive collection of Python scripts demonstrating data cleaning, aggregation, multi-source merging, and exploratory data analysis (EDA) using the **Pandas** library. It includes solutions to foundational data analysis problems, database interactions, and high-level analytical business questions.

The project is structured into key analytical tracks:
1. **End-to-End Sales Performance Tracking:** Synthesizing transactional attributes to uncover demographic trends.
2. **Relational Database Management (SQL + Python):** Integrating multi-table schemas (`Customers`, `Transactions`, and `Loans`) via SQLAlchemy and executed joins.
3. **Core Interview & Task Resolutions:** Implementing targeted logic to isolate specific operational metrics (e.g., active vs. inactive users, custom binning logic).

---

## Technical Python Skills Demonstrated

### 1. Data Cleaning & Transformation
* **Type Management:** Converting text strings into structural `datetime` formats using `pd.to_datetime()`.
* **Chronological Extraction:** Engineering temporal attributes using `.dt.month_name()` and `.dt.to_period('M')` for cohort analysis.
* **Conditional Segmentation:** Applying advanced logical hierarchies for binning continuous quantitative fields (e.g., categorizing ages into custom age cohorts sequentially).
* **Missing Value & Duplicate Resolution:** Handling empty rows with `.fillna()` and tracking schema health using `.isnull().sum()` and `.drop_duplicates()`.

### 2. Multi-Table Joins & Merges
* **Relational Mapping:** Utilizing Pandas `.merge()` to link records across independent domain schemas on key indexes like `customer_id`.
* **Database Connection:** Instantiating database connectivity pipelines using `create_engine` from **SQLAlchemy** to ingest transactional data tables directly into a Pandas environment.

### 3. Advanced Grouping & Business Aggregations
* **Dynamic Reports:** Creating descriptive summary matrices utilizing multi-argument calculations with `.groupby().agg()`.
* **Sorting & Thresholding:** Sorting value rankings and calculating quantile-based subsets (e.g., `.quantile(0.90)`) to isolate top 10% high-value consumers.

---

## Solved Business Case Questions Included
* How do you identify inactive customers who haven't transacted in the last 6 months?
* How do you isolate high-value customers based on top 10% spending thresholds?
* How do you track monthly rolling revenue trends and identify the single highest transactional order value?
* How do you analyze city-wise sales performance and distribution metrics?

---

## How to Explore the Script
1. View the source file `sales_and_customer_analysis.py` to inspect the clean, documented Pandas logic.
2. Ensure you have `pandas`, `sqlalchemy`, and `pymysql` installed in your environment to execute any of the independent data validation pipelines.
