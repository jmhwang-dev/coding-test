
select
    person_name
from (
    select
        person_name,
        total_weight,
        LAG(total_weight) OVER (ORDER BY total_weight) as prev_weight
    from (
        select
            person_name,
            sum(weight) over (order by turn) as total_weight
        from Queue
    )
)
where total_weight <= 1000
order by total_weight desc
limit 1

-- best
WITH cumulative AS (
    SELECT 
        person_name,
        turn,
        SUM(weight) OVER (ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_weight
    FROM 
        Queue
)
SELECT 
    person_name
FROM 
    cumulative
WHERE 
    cum_weight <= 1000
ORDER BY 
    turn DESC
LIMIT 1;