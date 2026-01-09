-- 멸종위기의 대장균 찾기
with recursive GENERATION as (
    select id, PARENT_ID, 1 as GENERATION
    from ECOLI_DATA
    where PARENT_ID is null
    
    union all
    
    select e.id, e.PARENT_ID, g.GENERATION + 1
    from GENERATION g
    inner join ECOLI_DATA e
    on g.id = e.parent_id
)

select count(*) as COUNT, GENERATION
from GENERATION
where id not in (
    select distinct PARENT_ID from GENERATION
    where PARENT_ID is not null
)
group by GENERATION