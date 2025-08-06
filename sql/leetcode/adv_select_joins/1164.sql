-- ans1

with UnderDate as (
    select
        product_id,
        max(change_date) as latest_date
    from Products
    where change_date <= '2019-08-16'
    group by product_id
),
DistinctProduct  as (
    select distinct(product_id)
    from Products
)
select
    dp.product_id,
    case when fp.price is null then 10 else fp.price end as price
from DistinctProduct dp
left join (
    select
        p_src.product_id,
        p_src.new_price as price 
    from Products p_src
    inner join UnderDate p_fil
    on
        p_src.product_id = p_fil.product_id and
        p_src.change_date = p_fil.latest_date
) fp
on dp.product_id = fp.product_id;

-- best
WITH max_dates AS (
    SELECT 
        product_id, 
        MAX(change_date) AS max_date
    FROM 
        Products
    WHERE 
        change_date <= '2019-08-16'
    GROUP BY 
        product_id
),
all_products AS (
    SELECT DISTINCT 
        product_id 
    FROM 
        Products
)
SELECT 
    a.product_id, 
    CASE 
        WHEN m.max_date IS NULL THEN 10 
        ELSE p.new_price 
    END AS price
FROM 
    all_products a
LEFT JOIN 
    max_dates m ON a.product_id = m.product_id
LEFT JOIN 
    Products p ON a.product_id = p.product_id AND m.max_date = p.change_date;