-- ans1

select
    product_name,
    sum(unit) as unit
from (
    select
        p.product_name,
        unit
    from Orders o
    left join Products p
    on o.product_id = p.product_id
    where '2020-02-01' <= order_date and order_date < '2020-03-01'
)
group by product_name
having sum(unit) >= 100