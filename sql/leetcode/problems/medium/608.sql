-- ans1
with ParentNode as (
    select p_id as id from Tree where p_id is not null
)

select id,
case
    when p_id is null then 'Root'
    when id in (select id from ParentNode) then 'Inner' else 'Leaf'
end as type
from Tree