-- ans
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    select s.salary
    from (
        select
            e.salary,
            dense_rank() over (order by e.salary) as rnk
        from Employee e
    ) s
    where s.rnk = N
    limit 1
  );
END;
$$ LANGUAGE plpgsql;

-- best
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT
        DISTINCT e.salary
    FROM Employee e
    ORDER BY e.salary DESC
    LIMIT 1 OFFSET N - 1
  );
END;
$$ LANGUAGE plpgsql;