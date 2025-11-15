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

-- best
SELECT 
    t.id,
    CASE 
        WHEN t.p_id IS NULL THEN 'Root'
        WHEN COUNT(c.id) = 0 THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree t
LEFT JOIN Tree c ON t.id = c.p_id
GROUP BY t.id, t.p_id
ORDER BY t.id;