-- ans1
with DupEmail as (
    select
        id,
        email,
        row_number() over (partition by email order by id asc) as dup_email
    from Person
)

delete from Person
where id in (select id from DupEmail where dup_email != 1)

-- ans2
delete from Person
where id not in (select min(id) from Person group by email)

-- best
DELETE FROM Person p1
WHERE EXISTS (
    SELECT 1
    FROM Person p2
    WHERE p2.email = p1.email
    AND p2.id < p1.id
);