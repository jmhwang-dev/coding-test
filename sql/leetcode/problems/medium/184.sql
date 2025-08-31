-- ans
select
    Department,
    Employee,
    Salary
from (select
    dense_rank() over (partition by departmentId order by salary desc) as rnk,
    e.name as Employee,
    e.salary as Salary,
    d.name as Department
from Employee e
left join Department d
on e.departmentId = d.id)
where rnk = 1