-- ans1
select unique_id, name from Employees left join EmployeeUNI 
on Employees.id = EmployeeUNI.id;

-- ans2
select unique_id, name
from Employees
left join EmployeeUNI using (id);