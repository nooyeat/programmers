-- 코드를 입력하세요
SELECT animal_type, count(animal_id) as count
from animal_ins
where animal_type in ('cat', 'dog')
group by 1
order by 1;