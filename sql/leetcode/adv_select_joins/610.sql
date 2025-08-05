-- Write your PostgreSQL query statement below
SELECT x, y, z,
       CASE WHEN z >= x + y OR y >= z + x OR x >= y + z THEN 'No'
            ELSE 'Yes'
       END AS triangle
FROM Triangle;