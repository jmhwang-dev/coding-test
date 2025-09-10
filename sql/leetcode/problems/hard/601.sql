-- ans
with RankedId as (
    select id, visit_date, people,
        rank() over(order by id) as rnk
    from Stadium
    where people >= 100
)
, Consecutive as (
    select id, visit_date, people, id - rnk as diff_rnk
    from RankedId
)

select id, visit_date, people
from Consecutive
where diff_rnk in (
    select diff_rnk
    from Consecutive
    group by diff_rnk having count(diff_rnk) > 2
)

-- best
WITH StadiumConsecutive AS (
    -- 1. 먼저 100명 이상인 날들만 필터링하고, 연속 여부를 판단할 그룹 ID를 생성합니다.
    SELECT 
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER(ORDER BY id) AS id_diff
    FROM 
        Stadium
    WHERE 
        people >= 100
),
GroupCounts AS (
    -- 2. 위에서 만든 그룹 ID(id_diff)별로 개수를 셉니다.
    SELECT
        id_diff,
        COUNT(*) AS consecutive_days
    FROM
        StadiumConsecutive
    GROUP BY
        id_diff
)
-- 3. 그룹별 개수가 3 이상인(즉, 3일 이상 연속된) 그룹의 모든 기록을 조회합니다.
SELECT 
    s.id,
    s.visit_date,
    s.people
FROM 
    StadiumConsecutive s
JOIN 
    GroupCounts g ON s.id_diff = g.id_diff
WHERE 
    g.consecutive_days >= 3
ORDER BY 
    s.visit_date;