-- Total Sales by Month
SELECT DATE_TRUNC('month', order_date) AS sales_month, SUM(price * quantity) AS total_revenue
FROM sales_data
GROUP BY sales_month
ORDER BY sales_month;

-- Top 5 Products by Revenue
SELECT product_name, SUM(price * quantity) AS revenue
FROM sales_data
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 5;

-- Customer Segmentation by Purchase Frequency
SELECT customer_id, COUNT(order_id) AS total_orders
FROM sales_data
GROUP BY customer_id
ORDER BY total_orders DESC;
