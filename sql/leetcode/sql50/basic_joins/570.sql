-- ans1
WITH employee_count_by_manager AS (
    SELECT 
        managerId
    FROM 
        Employee
    GROUP BY 
        managerId
    HAVING 
        COUNT(id) > 4
)
SELECT 
    name 
FROM (
    SELECT 
        * 
    FROM 
        employee_count_by_manager
    WHERE 
        managerId IN (
            SELECT 
                DISTINCT id 
            FROM 
                Employee
        )
) em
LEFT JOIN 
    Employee e
    ON 
        em.managerId = e.id;

-- ans2
WITH employee_count_by_manager AS (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(id) > 4
)
SELECT name 
FROM employee_count_by_manager em
JOIN Employee e
ON em.managerId = e.id;

-- ans3
select e.name
from Employee e
join (
    select managerId
    from Employee
    group by managerId
    having count(managerId) > 4
) target_m
on e.id = target_m.managerId

-- best
WITH manager_counts AS (
    SELECT 
        managerId
    FROM 
        Employee
    WHERE 
        managerId IS NOT NULL
    GROUP BY 
        managerId
    HAVING 
        COUNT(*) >= 5
)
SELECT 
    e.name
FROM 
    Employee e
INNER JOIN 
    manager_counts mc
    ON 
        e.id = mc.managerId;