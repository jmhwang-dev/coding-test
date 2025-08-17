-- ans
select *
from Users
WHERE mail ~ '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$'