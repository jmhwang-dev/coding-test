-- Write your PostgreSQL query statement below
select
    query_name,
    round(
        1.0 * sum(rating * 1.0 / position) / count(rating)
        ,2
    ) as quality,
    
    round(
        100.0 * sum(case when rating < 3 then 1 else 0 end) / count(rating)
        ,2
    ) as poor_query_percentage

from Queries
group by query_name;


-- best
SELECT
    query_name,
    ROUND(AVG(rating * 1.0 / position), 2) AS quality,
    ROUND(100.0 * AVG(CASE WHEN rating < 3 THEN 1.0 ELSE 0 END), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;