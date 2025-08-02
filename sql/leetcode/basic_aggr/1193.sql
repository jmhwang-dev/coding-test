SELECT
    -- TO_CHAR(trans_date, 'YYYY-MM') AS month, -- postgres 전용 함수
    EXTRACT(YEAR FROM trans_date) || '-' || 
    LPAD(EXTRACT(MONTH FROM trans_date)::TEXT, 2, '0') AS month,
    country,
    count(*) as trans_count,
    count(case when state = 'approved' then 1 else null end ) as approved_count,
    sum(amount) as trans_total_amount,
    sum(case when state = 'approved' then amount else 0 end ) as approved_total_amount
FROM Transactions
GROUP BY month, country