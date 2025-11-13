-- ans 1
with UniqueSoldProductInFirstQuater as (
    select product_id
    from Sales
    group by product_id
    having
    min(sale_date) between '2018-12-31' and '2019-04-01' and
    max(sale_date) between '2018-12-31' and '2019-04-01'
)

select p.product_id, p.product_name
from UniqueSoldProductInFirstQuater u
join Product p
on p.product_id = u.product_id


-- ans2
select p.product_id, p.product_name
from Sales s
join Product p on p.product_id = s.product_id
group by p.product_id, p.product_name
having '2018-12-31' < min(sale_date) and max(sale_date) < '2019-04-01'