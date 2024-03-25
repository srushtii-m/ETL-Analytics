-- Sales Performance Over Time
SELECT
  o.order_year,
  o.order_month,
  SUM(s.order_item_total) AS TotalSales
FROM `scm-etl.scm_data_etl.fact_sales` AS s
JOIN `scm-etl.scm_data_etl.dim_order` AS o ON s.o_id = o.o_id
GROUP BY o.order_year, o.order_month
ORDER BY o.order_year, o.order_month;

-- Customer Sales Analysis
SELECT
  c.customer_segment,
  COUNT(DISTINCT c.c_id) AS NumberOfCustomers,
  SUM(s.order_item_total) AS TotalSales
FROM `scm-etl.scm_data_etl.fact_sales` AS s
JOIN `scm-etl.scm_data_etl.dim_customer` AS c ON s.c_id = c.c_id
GROUP BY c.customer_segment;

-- Product Category Performance
SELECT
  p.category_name,
  COUNT(s.p_id) AS UnitsSold,
  SUM(s.order_item_total) AS TotalSales
FROM `scm-etl.scm_data_etl.fact_sales` AS s
JOIN `scm-etl.scm_data_etl.dim_product` AS p ON s.p_id = p.p_id
GROUP BY p.category_name
ORDER BY TotalSales DESC;

-- Impact of Discounts on Sales
SELECT
  s.order_item_discount_rate,
  AVG(s.order_item_total) AS AvgOrderValue
FROM `scm-etl.scm_data_etl.fact_sales` AS s
GROUP BY s.order_item_discount_rate
ORDER BY s.order_item_discount_rate;

-- Sales by Geographic Location
SELECT
  o.order_state,
  SUM(s.order_item_total) AS TotalSales
FROM `scm-etl.scm_data_etl.fact_sales` AS s
JOIN `scm-etl.scm_data_etl.dim_order` AS o ON s.o_id = o.o_id
GROUP BY o.order_state
ORDER BY TotalSales DESC;

-- Sales and Shipping Efficiency
SELECT
  sh.shipping_mode,
  AVG(sh.days_for_shipping) AS AvgShippingDays,
  SUM(s.order_item_total) AS TotalSales
FROM `scm-etl.scm_data_etl.fact_sales` AS s
JOIN `scm-etl.scm_data_etl.dim_shipping` AS sh ON s.s_id = sh.s_id
GROUP BY sh.shipping_mode;

--
CREATE TABLE `scm-etl.scm_data.sales_analytics` AS
SELECT
  f.sales_id,
  c.customer_id,
  c.customer_segment,
  p.product_name,
  p.category_name,
  d.department_name,
  o.order_date,
  s.shipping_date,
  s.days_for_shipping,
  f.order_item_quantity,
  f.order_item_total,
  f.benefit_per_order,
  f.order_item_discount,
  f.order_item_discount_rate,
  (f.order_item_total - f.order_item_discount) AS net_sales,
  TIMESTAMP_DIFF(s.shipping_date, o.order_date, DAY) AS shipping_delay
FROM
  `scm-etl.scm_data.fact_sales` f
JOIN
  `scm-etl.scm_data.dim_customer` c ON f.c_id = c.c_id
JOIN
  `scm-etl.scm_data.dim_product` p ON f.p_id = p.p_id
JOIN
  `scm-etl.scm_data.dim_order` o ON f.o_id = o.o_id
JOIN
  `scm-etl.scm_data.dim_department` d ON f.d_id = d.d_id
JOIN
  `scm-etl.scm_data.dim_shipping` s ON f.s_id = s.s_id
