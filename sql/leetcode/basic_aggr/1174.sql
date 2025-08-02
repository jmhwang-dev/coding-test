-- ans
with FirstOrderDate as (
    select
    customer_id,
    min(order_date) as first_order_date
    from Delivery d1
    group by customer_id
)

select
round(
    100.0 * avg(case when first_order_date = customer_pref_delivery_date then 1 else 0 end)
    , 2) as immediate_percentage
from FirstOrderDate fd
left join Delivery d
on fd.customer_id = d.customer_id and fd.first_order_date = d.order_date;


-- best1
SELECT 
    ROUND(
        AVG(CASE WHEN is_immediate THEN 1.0 ELSE 0.0 END) * 100, 
        2
    ) AS immediate_percentage
FROM (
    SELECT DISTINCT
        customer_id,
        FIRST_VALUE(order_date = customer_pref_delivery_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS is_immediate
    FROM Delivery
) t;

-- best2
WITH first_orders AS (
    SELECT 
        customer_id,
        order_date,
        customer_pref_delivery_date,
        RANK() OVER (PARTITION BY customer_id ORDER BY order_date) AS rnk
    FROM Delivery
)
SELECT 
    ROUND(
        AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1.0 ELSE 0.0 END) * 100, 
        2
    ) AS immediate_percentage
FROM first_orders
WHERE rnk = 1;