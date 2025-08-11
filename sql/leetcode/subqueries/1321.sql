-- best
with DailySum as (
    select visited_on, sum(amount) as total_amount
    from Customer
    group by visited_on
),
MovingAverageSum as (
    select
        visited_on,
        sum(total_amount) over (
            order by visited_on rows between 6 preceding and current row) as amount,
        round( avg(total_amount) over (
            order by visited_on rows between 6 preceding and current row), 2 ) as average_amount,
        ROW_NUMBER() OVER (ORDER BY visited_on) AS row_num
    from DailySum
)

select
    visited_on,
    amount,
    average_amount
from MovingAverageSum
where row_num >= 7;