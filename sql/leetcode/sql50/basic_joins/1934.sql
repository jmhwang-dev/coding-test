-- Write your PostgreSQL query statement below
with
all_log as (
    select user_id, action
    from Signups
    full outer join Confirmations
    using(user_id)
),
request_cnt as (
    select user_id, count(*) as req_cnt
    from all_log
    group by user_id
),
confirmed_cnt as (
    select user_id, count(action) as confirm_cnt
    from all_log
    where action = 'confirmed'
    group by user_id
),
cnt_table as (
    select user_id, req_cnt, COALESCE(confirm_cnt, 0) as conf_cnt
    from request_cnt r
    left join confirmed_cnt c
    using(user_id)
)

select user_id, round(conf_cnt/req_cnt::numeric, 2) as confirmation_rate
from cnt_table;

-- best
SELECT 
    s.user_id,
    ROUND(
        COALESCE(
            AVG(CASE WHEN c.action = 'confirmed' THEN 1.0 ELSE 0.0 END),
            0.0
        ),
        2
    ) AS confirmation_rate
FROM 
    Signups s
LEFT JOIN 
    Confirmations c
    ON s.user_id = c.user_id
GROUP BY 
    s.user_id;