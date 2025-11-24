-- ans1
select
buyer_id,
join_date,
sum(orders_in_2019) as orders_in_2019
from(
    select
    u.user_id as buyer_id,
    u.join_date,
    case when extract(year from order_date) = 2019 then 1 else 0 end as orders_in_2019
from Users u
left join Orders o
on o.buyer_id = u.user_id
)
group by buyer_id, join_date
order by buyer_id


-- best
SELECT 
    u.user_id AS buyer_id,
    u.join_date,
    COUNT(o.order_id) AS orders_in_2019
FROM 
    Users u
LEFT JOIN 
    Orders o ON u.user_id = o.buyer_id AND extract(year from o.order_date) = 2019
GROUP BY 
    u.user_id, u.join_date
ORDER BY 
    u.user_id;