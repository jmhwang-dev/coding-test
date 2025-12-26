-- ans1
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

-- ans2
with RequestCount as (
    select s.user_id, count(c.time_stamp)::numeric as requtest_count
    from Signups s
    left join Confirmations c
    on s.user_id = c.user_id
    group by s.user_id
),

ConfirmedCount as (
    select user_id, count(user_id)::numeric as confirmed_count
    from Confirmations
    where action = 'confirmed'
    group by user_id
)

select
    r.user_id,
    coalesce(round(confirmed_count/requtest_count, 2), 0) as confirmation_rate
from RequestCount r
left join ConfirmedCount c
on r.user_id = c.user_id

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