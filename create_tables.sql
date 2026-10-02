CREATE SCHEMA IF NOT EXISTS `your-gcp-project-id.customer360`;

CREATE TABLE IF NOT EXISTS `your-gcp-project-id.customer360.dim_customer`
(
    customer_id INT64,
    customer_name STRING,
    email STRING,
    country STRING,
    customer_type STRING,
    updated_timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `your-gcp-project-id.customer360.fact_orders`
(
    order_id INT64,
    customer_id INT64,
    product_id INT64,
    quantity INT64,
    amount FLOAT64,
    status STRING,
    updated_timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `your-gcp-project-id.customer360.fact_payments`
(
    payment_id INT64,
    customer_id INT64,
    order_id INT64,
    amount FLOAT64,
    payment_status STRING,
    payment_method STRING,
    updated_timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `your-gcp-project-id.customer360.customer_360`
(
    customer_id INT64,
    customer_name STRING,
    email STRING,
    country STRING,
    customer_type STRING,
    total_orders INT64,
    total_order_amount FLOAT64,
    total_paid_amount FLOAT64,
    last_order_timestamp TIMESTAMP,
    last_payment_timestamp TIMESTAMP
);
