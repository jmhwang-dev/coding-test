-- ans1
select
    case when count(salary) = 2 then min(salary) else null end as SecondHighestSalary
from (
    select distinct salary
    from Employee
    order by salary desc
    limit 2
)

-- best1
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);

-- best2
SELECT 
    (SELECT DISTINCT salary
     FROM Employee
     ORDER BY salary DESC
     LIMIT 1 OFFSET 1) AS SecondHighestSalary;

-- best3
SELECT 
    (SELECT salary
     FROM (
         SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
         FROM Employee
     ) t
     WHERE rnk = 2
     LIMIT 1) AS SecondHighestSalary;