-- ans 1
select
    product_id,
    year as first_year,
    quantity,
    price
from 
(
    select
        product_id,
        year,
        quantity,
        price,
        rank() over (partition by product_id order by year)
    from Sales
)
where rank = 1;

-- ans2
select
    s.product_id,
    s.year as first_year,
    s.quantity,
    s.price
from Sales s
inner join 
(
    select
        product_id,
        min(year) as first_year
    from Sales
    group by product_id
) f
on s.product_id = f.product_id and s.year = f.first_year;

-- best
SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
WHERE (s.product_id, s.year) IN (
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id
);