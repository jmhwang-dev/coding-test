-- ans
with RankedNums as (
    select id, num, rank() over (partition by num order by id) from Logs
)

select distinct num as ConsecutiveNums
from (
    select num, (id - rank) as diff_rank
    from RankedNums
)
group by num, diff_rank
having count((num, diff_rank)) > 2

-- best
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
           LAG(num, 1) OVER (ORDER BY id) AS prev_num,
           LAG(num, 2) OVER (ORDER BY id) AS prev_num2
    FROM Logs
) t
WHERE num = prev_num AND prev_num = prev_num2;