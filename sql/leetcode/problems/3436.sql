select
    user_id,
    email
from Users
where email ~ '^[a-zA-Z0-9_]+@[a-z]+\.com$'