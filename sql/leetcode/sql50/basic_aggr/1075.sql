-- Write your PostgreSQL query statement below
select
    project_id,
    round(avg(experience_years), 2) as average_years
from Project p
left join Employee e
on p.employee_id = e.employee_id
group by project_id
order by project_id;

-- best
SELECT
    p.project_id,
    COALESCE(ROUND(AVG(e.experience_years), 2), 0) AS average_years
FROM Project p
LEFT JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY p.project_id
ORDER BY p.project_id;