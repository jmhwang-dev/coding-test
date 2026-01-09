SELECT B.CATEGORY, SUM(BS.SALES) AS TOTAL_SALES
FROM BOOK_SALES BS
INNER JOIN BOOK B ON BS.BOOK_ID = B.BOOK_ID -- 1. 그냥 붙인다
WHERE BS.SALES_DATE LIKE '2022-01%'         -- 2. 날짜 거른다
GROUP BY B.CATEGORY                         -- 3. 묶는다
ORDER BY B.CATEGORY ASC;

-- -- 코드를 입력하세요
-- select t.category, sum(t.sales) as TOTAL_SALES
-- from (
--     select b.category, bs.sales
--     from (
--         SELECT BOOK_ID, SALES
--         FROM BOOK_SALES
--         WHERE
--         EXTRACT(YEAR FROM SALES_DATE) = 2022 AND
--         EXTRACT(MONTH FROM SALES_DATE) = 1
--     ) bs
--     left join BOOK b
--     # using(b.BOOK_ID = bs.BOOK_ID)
--     using(BOOK_ID)
-- ) t
-- group by CATEGORY
-- order by CATEGORY ASC