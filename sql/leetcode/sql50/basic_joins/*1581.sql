-- ans1
select
    customer_id,
    count(*) - count(transaction_id) as count_no_trans
from Visits
left join Transactions using (visit_id)
group by customer_id
having count(*) - count(transaction_id) > 0;

-- ans2 *
select
    customer_id,
    count(*) AS count_no_trans 
from Visits
left join Transactions using (visit_id)
where transaction_id is null
group by customer_id;