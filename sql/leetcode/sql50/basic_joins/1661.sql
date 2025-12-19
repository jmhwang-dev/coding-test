-- ans1
SELECT 
    machine_id, 
    ROUND(avg(run_time)::numeric, 3) AS processing_time
FROM (
    SELECT 
        s.machine_id, 
        s.process_id, 
        (e.timestamp - s.timestamp) AS run_time
    FROM (
        SELECT * 
        FROM Activity 
        WHERE activity_type = 'start'
    ) AS s
    LEFT JOIN (
        SELECT * 
        FROM Activity 
        WHERE activity_type = 'end'
    ) AS e
    ON (s.machine_id, s.process_id) = (e.machine_id, e.process_id)
) AS sub
GROUP BY 
    machine_id;

-- ans2
select s.machine_id, round(avg(e.timestamp - s.timestamp)::numeric, 3) as processing_time
from Activity s
join Activity e
on s.machine_id = e.machine_id and s.process_id = e.process_id
where s.activity_type = 'start' and e.activity_type = 'end'
group by s.machine_id;

-- ans3
with StartTimestamp as (
    select *
    from Activity
    where activity_type = 'start'
),

EndTimestamp as (
    select *
    from Activity
    where activity_type = 'end'
),

ProcessingTime as (
    select
        e.machine_id,
        e.timestamp - s.timestamp as processing_time
    from EndTimestamp e
    left join StartTimestamp s
    on e.machine_id = s.machine_id and e.process_id = s.process_id
)

select machine_id, round(avg(processing_time)::numeric, 3) as processing_time
from ProcessingTime
group by machine_id


-- best1 가독성 + 정석 (Self-Join)
SELECT 
    a1.machine_id, 
    ROUND(AVG(a2.timestamp - a1.timestamp)::numeric, 3) AS processing_time
FROM 
    Activity a1
JOIN 
    Activity a2 
ON 
    a1.machine_id = a2.machine_id 
    AND a1.process_id = a2.process_id
    AND a1.activity_type = 'start' 
    AND a2.activity_type = 'end'
GROUP BY 
    a1.machine_id;

-- best2 성능 중심
SELECT 
    a1.machine_id, 
    ROUND(AVG(a2.timestamp - a1.timestamp)::numeric, 3) AS processing_time
FROM 
    Activity a1
JOIN 
    Activity a2 
ON 
    a1.machine_id = a2.machine_id 
    AND a1.process_id = a2.process_id
    AND a1.activity_type = 'start' 
    AND a2.activity_type = 'end'
GROUP BY 
    a1.machine_id;