select author_id as id from Views
where author_id = viewer_id
group by author_id
having count(view_date) > 0
order by id;

---
select distinct author_id as id from Views
where author_id = viewer_id
order by id;