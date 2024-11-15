# -- 코드를 입력하세요
SELECT ri.rest_id, rest_name, food_type, favorites, address, round(avg(review_score),2) as score
from rest_info as ri, rest_review as rr
where ri.address like '서울%' and ri.rest_id = rr.rest_id
group by ri.rest_id
order by score desc, ri.favorites desc;