-- Write your PostgreSQL query statement below

with Sequence as (
    select
        id,
        student,
        lag(id) over (order by id) as prev_id,
        lead(id) over (order by id) as next_id
    from
        Seat
),
LastId as (
    select id
    from Seat
    order by id desc
    limit 1
)

select
    id,
    case
        when id % 2 = 1 and last_id is not null then cur_student
        when id % 2 = 1 then next_student
        when id % 2 = 0 then prev_student
    end as student
from (
    select 
        cur.id as id,
        cur.student as cur_student,
        seq2.student as prev_student,
        seq1.student as next_student,
        l.id as last_id
    from Seat cur
    left join Sequence seq1
    on cur.id = seq1.prev_id
    left join Sequence seq2
    on cur.id = seq2.next_id
    left join LastId as l
    on cur.id = l.id
)

-- best
SELECT 
    id,
    CASE 
        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM seat) THEN student
        WHEN id % 2 = 1 THEN (SELECT student FROM seat WHERE id = s.id + 1)
        ELSE (SELECT student FROM seat WHERE id = s.id - 1)
    END AS student
FROM seat s
ORDER BY id;