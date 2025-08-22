-- ans1
with CountTIV2015 as (
    select
        tiv_2015,
        count(tiv_2015) as count_same_tiv_2015
    from Insurance
    group by tiv_2015
),
CheckSameTIV2015 as (
    select 
        pid,
        tiv_2015,
        tiv_2016,
        lat,
        lon,
        case
            when tiv_2015 in (select tiv_2015 from CountTIV2015 where count_same_tiv_2015 > 1) then True
            else False
        end as has_2015
    from Insurance
),
CheckLocation as (
    select
        case when count(*) = 1 then pid else null end as pid
    from Insurance
    group by lat, lon
)

select round(sum(s.tiv_2016), 2) as tiv_2016
from CheckLocation l
inner join CheckSameTIV2015 s
on l.pid = s.pid
where s.has_2015 = 1;

-- ans2
# Write your MySQL query statement below

with DupTIV2015 as (
    select
        case when count(tiv_2015) > 1 then tiv_2015 end tiv_2015
    from Insurance
    group by tiv_2015
),

InDupTIV2015 as (
    select *
    from Insurance
    where tiv_2015 in (select * from DupTIV2015)
),

UniqueLocationPID as (
    select
        case when count(*) = 1 then pid end as pid
    from Insurance
    group by lat, lon
)

select round(sum(i.tiv_2016), 2) as tiv_2016
from Insurance i
inner join InDupTIV2015 id
on i.pid = id.pid
inner join UniqueLocationPID ul
on i.pid = ul.pid

-- ans3
with DupTIV2015 as (
    select tiv_2015
    from Insurance
    group by tiv_2015
    having count(tiv_2015) > 1
),

InDupTIV2015 as (
    select *
    from Insurance
    where tiv_2015 in (select * from DupTIV2015)
),

UniqueLocationPID as (
    select pid
    from Insurance
    group by lat, lon
    having count(*) = 1
)

select round(sum(i.tiv_2016), 2) as tiv_2016
from Insurance i
inner join InDupTIV2015 id
on i.pid = id.pid
inner join UniqueLocationPID ul
on i.pid = ul.pid


-- best
SELECT ROUND(SUM(tiv_2016)::numeric, 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);