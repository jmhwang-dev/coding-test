-- Write your PostgreSQL query statement below

with JoinedRecord as (
    select
        m.title,
        u.name,
        rating,
        created_at
    from MovieRating mr
    left join Movies m
    on mr.movie_id = m.movie_id
    left join Users u
    on mr.user_id = u.user_id
),
CountRate as (
    select
        name,
        count(title)
    from JoinedRecord
    group by name
    order by count desc, name asc
    limit 1
),
AverageRate as (
    select
        title,
        avg(rating)
    from JoinedRecord
    where '2020-02-01' <= created_at and created_at < '2020-03-01'
    group by title
    order by avg desc, title asc
    limit 1
)

select name as results from CountRate
union all
select title as results from AverageRate