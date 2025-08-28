-- ans1 - best
select e.name as Employee
from Employee e
left join Employee m
on e.managerId = m.id
where e.salary > m.salary

-- ans2

select e.name as Employee
from Employee e
where e.salary > (select m.salary from Employee m where m.id = e.managerId)