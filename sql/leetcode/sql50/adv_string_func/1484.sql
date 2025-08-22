-- ans1

select
    sell_date,
    count(product) as num_sold,
    STRING_AGG(product, ',') as products
from (
    select distinct sell_date, product
    from Activities
    order by sell_date, product
)
group by sell_date

-- best
select
    sell_date,
    count(distinct product) as num_sold,
    STRING_AGG(distinct product, ',' ORDER BY product) as products
from Activities
group by sell_date
order by sell_date