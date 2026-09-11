# E-commerce Sales & Customer Analysis

A practical Python data analysis project for an e-commerce business. The project demonstrates data quality checks, KPI calculation, sales/profit analysis, grouping, reporting, and business visualization using **Python, Pandas, and Matplotlib**.

> **Dataset note:** The dataset is synthetic and was created for portfolio/practice purposes. It does not contain real customer information.

## Business Questions

This project answers questions such as:

- What are total sales, profit, orders, and units sold?
- How does sales performance change month by month?
- Which product categories generate the most revenue and profit?
- Which cities contribute the most sales?
- Which products are the strongest performers?
- Which payment methods are most commonly used?
- Does the dataset contain missing values or duplicate rows?

## Tools & Skills

- Python
- Pandas
- NumPy
- Matplotlib
- CSV data handling
- Data quality checks
- GroupBy aggregation
- KPI analysis
- Business reporting
- Data visualization

## Project Structure

```text
ecommerce-sales-customer-analysis/
│
├── analysis.py
├── requirements.txt
├── README.md
│
├── data/
│   └── ecommerce_sales.csv
│
└── outputs/
    ├── category_performance.csv
    ├── city_performance.csv
    ├── monthly_performance.csv
    ├── payment_method_analysis.csv
    ├── product_performance.csv
    ├── monthly_sales_trend.png
    ├── sales_by_category.png
    ├── sales_by_city.png
    └── top_products_by_profit.png
```

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the analysis

```bash
python analysis.py
```

The script prints the main KPIs and data-quality checks, then saves summary CSV files and charts in the `outputs` folder.

## Key Portfolio Takeaways

The analysis is designed to demonstrate an end-to-end workflow:

**Raw business data → quality checks → KPI analysis → grouped analysis → visual reporting → business insights**

## Sample Business Interpretation

When presenting this project to a client, focus on the business outcome rather than only the code. For example:

- Identify high-performing categories and products.
- Compare sales contribution across cities.
- Track monthly sales movement.
- Use profit alongside revenue to avoid judging performance by sales alone.
- Review payment-method usage when planning operational improvements.

## Disclaimer

This is a portfolio project using synthetic e-commerce data. It is intended to demonstrate analytical workflow and technical skills.
