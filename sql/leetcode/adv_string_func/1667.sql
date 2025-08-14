-- ans1

select
    user_id,
    concat(first_char, rest_str) as name
from (
    select
        user_id,
        upper(substring(name from 1 for 1)) as first_char,
        lower(substring(name from 2)) as rest_str
    from Users
) 
order by user_id

-- ans2
select
    user_id,
    concat(
        upper(substring(name from 1 for 1)), 
        lower(substring(name from 2)) ) as name
from Users
order by user_id