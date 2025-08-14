-- latest ans1
-- Write your PostgreSQL query statement below



select
    d.name as Department,
    r.name as Employee,
    r.salary as Salary
from Department d
right join (
    select
        departmentId,
        name,
        salary,
        DENSE_RANK() over (partition by departmentId order by salary desc) as rank
    from Employee
) r
on d.id = r.departmentId
where r.rank < 4
order by Department, Salary desc

-- old ans
WITH ranked_employees AS (
    SELECT d.name AS department,
           e.name AS employee,
           e.salary AS salary,
           DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS rank
    FROM Employee e
    INNER JOIN Department d ON e.departmentId = d.id
)
SELECT department, employee, salary
FROM ranked_employees
WHERE rank <= 3
ORDER BY department, rank;

---

-- SELECT "Department", "Employee", "Salary"
-- FROM (
--     SELECT d.name AS "Department", 
--            e.name AS "Employee", 
--            e.salary AS "Salary",
--            DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS rank
--     FROM Employee e
--     INNER JOIN Department d ON e.departmentId = d.id
-- ) ranked
-- WHERE rank <= 3;