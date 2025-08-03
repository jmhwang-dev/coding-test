-- ans1
with DeduplicatedActivity as (
    select  distinct user_id, session_id, activity_date
    from Activity
    where
    cast('2019-07-27' as date) - interval '30 days' < activity_date
    and
    activity_date <= cast('2019-07-27' as date)
)

select
    activity_date as day,
    count(distinct user_id) as active_users
from
    DeduplicatedActivity
group by activity_date;

-- ans2
select
    activity_date as day,
    count(distinct user_id) as active_users
from
    Activity
group by
    activity_date
having
    cast('2019-07-27' as date) - interval '30 days' < activity_date
    and
    activity_date <= cast('2019-07-27' as date)

-- ans3
select
    activity_date as day,
    count(distinct user_id) as active_users
from
    Activity
where 
    cast('2019-07-27' as date) - interval '30 days' < activity_date
    and
    activity_date <= cast('2019-07-27' as date)
group by
    activity_date


-- best
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date;