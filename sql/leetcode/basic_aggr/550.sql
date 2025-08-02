with RankedLoginDate as (
    select
        player_id,
        event_date,
        rank() over (partition by player_id order by event_date)
    from Activity
),
FirstLoginDate as (
    select *
    from RankedLoginDate
    where rank = 1
),
SecondLoginDate as (
    select *
    from RankedLoginDate
    where rank = 2
),
ImmediateLoginUser as (
    select s.player_id
    from SecondLoginDate s
    left join FirstLoginDate f
    on s.player_id = f.player_id
    where s.event_date - f.event_date = 1
)

select round(1.0 * count(distinct i.player_id) / count(distinct a.player_id), 2) as fraction
from Activity a
left join ImmediateLoginUser i
on i.player_id = a.player_id;

-- best
SELECT 
    ROUND(
        AVG(CASE WHEN next_date = event_date + INTERVAL '1 day' THEN 1.0 ELSE 0.0 END), 
        2
    ) AS fraction
FROM (
    SELECT 
        player_id,
        event_date,
        LEAD(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS next_date
    FROM Activity
    WHERE ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) = 1
) t;