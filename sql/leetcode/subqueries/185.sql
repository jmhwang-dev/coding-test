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