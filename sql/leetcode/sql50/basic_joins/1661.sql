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

-- ans2*
select s.machine_id, round(avg(e.timestamp - s.timestamp)::numeric, 3) as processing_time
from Activity s
join Activity e
on s.machine_id = e.machine_id and s.process_id = e.process_id
where s.activity_type = 'start' and e.activity_type = 'end'
group by s.machine_id;