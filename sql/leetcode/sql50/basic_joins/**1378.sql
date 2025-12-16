-- ans1
select unique_id, name from Employees left join EmployeeUNI 
on Employees.id = EmployeeUNI.id;

-- ans2 *
select unique_id, name
from Employees
left join EmployeeUNI using (id);


---

--- ans1
SELECT w1.id
FROM Weather w1
JOIN Weather w2
    ON w1.recordDate - w2.recordDate = 1 -- 날짜 빼기 연산
WHERE w1.temperature > w2.temperature;

-- ans2
SELECT w1.id
FROM Weather w1
JOIN Weather w2
    -- w1(오늘)은 w2(어제) + 1일이어야 함
    ON w1.recordDate = w2.recordDate + interval '1 day'
WHERE w1.temperature > w2.temperature;

-- ans3
select id
from (
    select id,
        (temperature - lag(temperature) over (order by recordDate asc)) as diff_tmp,
        (recordDate - lag(recordDate) over (order by recordDate asc)) as diff_date
    from Weather
)
where diff_tmp > 0 and diff_date = 1

-- best (time-cost: self join > Window Function(lag))
WITH prev_weather_data AS (
    SELECT 
        id,
        recordDate,
        temperature,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp
    FROM Weather
)
SELECT id
FROM prev_weather_data
WHERE 
    (recordDate - prev_date) = 1
    AND temperature > prev_temp;