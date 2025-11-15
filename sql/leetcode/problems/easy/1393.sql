-- ans1
select stock_name, (sell_price - buy_price) as capital_gain_loss
from 
(
    select buy.stock_name, buy_price, sell_price
    from (
        select stock_name, sum(price) as buy_price
        from Stocks
        where operation = 'Buy'
        group by stock_name
    ) buy
    join(
        select stock_name, sum(price) as sell_price
        from Stocks
        where operation = 'Sell'
        group by stock_name
    ) sell
    on buy.stock_name = sell.stock_name
)


-- ans2
select
    stock_name,
    sum(case when operation = 'Buy' then price * -1 else price end) as capital_gain_loss
from Stocks
group by stock_name