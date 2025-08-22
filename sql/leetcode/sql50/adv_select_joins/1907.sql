-- ans1
WITH Categories AS (
    SELECT category
    FROM (
        VALUES 
        ('Low Salary'),
        ('Average Salary'),
        ('High Salary')
    ) AS t(category)
),
SalaryCategory as (
    select
        account_id,
        case
            when income < 20000  then 'Low Salary'
            when 20000 <= income and income <= 50000 then 'Average Salary'
            when 50000 < income then 'High Salary'
        end as salary_category
    from Accounts

),
CategoryAccountsCount as (
    select
        salary_category as category,
        count(account_id) as accounts_count
    from
        SalaryCategory
    group by salary_category
)

select
    c.category,
    coalesce(accounts_count, 0) as accounts_count
from Categories c
left join CategoryAccountsCount ca
on c.category = ca.category;

-- ans2
WITH Categories AS (
    SELECT category
    FROM (VALUES ('Low Salary'), ('Average Salary'), ('High Salary')) AS t(category)
),
SalaryCategory AS (
    SELECT 
        CASE 
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category
    FROM Accounts
)
SELECT
    c.category,
    COUNT(s.category)::integer AS accounts_count
FROM Categories c
LEFT JOIN SalaryCategory s ON c.category = s.category
GROUP BY c.category;

-- best
select
    'Low Salary' as category,
    count(account_id) as accounts_count
from Accounts
where income < 20000
union
select
    'Average Salary' as category,
    count(account_id) as accounts_count
from Accounts
where income between 20000 and 50000
union
select
    'High Salary' as category,
    count(account_id) as accounts_count
from Accounts
where income > 50000