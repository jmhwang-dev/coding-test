-- ans
with Purchase as (
  select
      product_id,
      coalesce(price, 0) as price,
      coalesce(units, 0) as units
  from Prices
  left join UnitsSold
  using(product_id)
  where purchase_date is null or (start_date <= purchase_date and purchase_date <= end_date)
)
select
  product_id,
  (case when sum(units) <> 0
    then round(sum(price * units)::numeric / sum(units)::numeric, 2)
    else 0
  end) as average_price
from Purchase
group by product_id;

-- best
with Purchase as (
  select
      Prices.product_id,
      price,
      coalesce(units, 0) as units
  from Prices
  left join UnitsSold
  on Prices.product_id = UnitsSold.product_id
  and start_date <= purchase_date and purchase_date <= end_date
)
select
  product_id,
  (case when sum(units) <> 0
    then round(cast(sum(price * units) as numeric) / cast(sum(units) as numeric), 2)
    else 0
  end) as average_price
from Purchase
group by product_id;