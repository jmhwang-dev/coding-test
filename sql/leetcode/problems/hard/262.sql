-- ans
with TripsInDateRange as (
select
client_id,
driver_id,
request_at,
case when status = 'completed' then 0 else 1 end as status
from Trips
where request_at::Date between '2013-10-01' and '2013-10-03'
)
, NotBannedClient as (
select users_id
from Users
where banned = 'No' and role = 'client'
)
, NotBannedDriver as (
select users_id
from Users
where banned = 'No' and role = 'driver'
)
, NotBannedUsersInDateRange as (
select *
from TripsInDateRange
where
client_id in (select * from NotBannedClient) and
driver_id in (select * from NotBannedDriver)
)

select
request_at as Day,
round(avg(status)::numeric, 2) as "Cancellation Rate"
from NotBannedUsersInDateRange
group by request_at

-- best

SELECT
    T.request_at AS "Day",
    ROUND(
        -- 취소된 요청의 합계를 총 요청 수로 나누어 취소율 계산
        SUM(CASE WHEN T.status != 'completed' THEN 1 ELSE 0 END)::numeric / COUNT(T.id), 2
    ) AS "Cancellation Rate"
FROM
    Trips AS T
-- Users 테이블과 두 번 JOIN하여 client와 driver의 차단 여부를 확인
JOIN
    Users AS C ON T.client_id = C.users_id
JOIN
    Users AS D ON T.driver_id = D.users_id
WHERE
    -- client와 driver가 모두 차단되지 않은 경우만 필터링
    C.banned = 'No' AND D.banned = 'No'
    -- 날짜 범위 필터링
    AND T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY
    T.request_at
ORDER BY
    T.request_at;