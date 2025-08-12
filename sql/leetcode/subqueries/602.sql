
-- ans1
with NotNullAccept as (
    select requester_id, accepter_id from RequestAccepted where accept_date is not null
),
ReqFriend as (
    select
        requester_id as id,
        count(accepter_id) as count_friend
    from NotNullAccept
    group by requester_id
),
AccFrined as (
    select
        accepter_id as id,
        count(requester_id) as count_friend
    from NotNullAccept
    group by accepter_id
)

select id, num
from (
select 
    id,
    sum(count_friend) as num
from(
    select * from AccFrined
    union all
    select * from ReqFriend
) a
group by id
) a2
order by num desc
limit 1

-- ans2
with NotNullAccept as (
    select requester_id, accepter_id from RequestAccepted where accept_date is not null
)

select
    requester_id as id,
    count(accepter_id) as num
from (
    select requester_id, accepter_id from NotNullAccept
    union all
    select accepter_id, requester_id from NotNullAccept
) a1
group by requester_id
order by num desc
limit 1