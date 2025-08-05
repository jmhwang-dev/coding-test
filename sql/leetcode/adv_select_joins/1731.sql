-- Write your PostgreSQL query statement below
select m.employee_id, e.name, m.reports_count, m.average_age
from Employees e
right join (
    select
        reports_to as employee_id,
        count(employee_id) as reports_count,
        round(avg(age)) as average_age
    from Employees
    group by reports_to
    having count(employee_id) >= 1 and reports_to is not null
) m
on e.employee_id = m.employee_id
order by m.employee_id;

-- best
SELECT 
    m.employee_id, 
    m.name, 
    COUNT(e.employee_id) AS reports_count, 
    ROUND(AVG(e.age)) AS average_age
FROM Employees m
INNER JOIN Employees e ON e.reports_to = m.employee_id
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id;