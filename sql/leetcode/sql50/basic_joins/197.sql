-- ans
select yest.id from Weather cur
left join Weather yest on cur.recordDate = yest.recordDate - Interval '1day'
where cur.temperature < yest.temperature;