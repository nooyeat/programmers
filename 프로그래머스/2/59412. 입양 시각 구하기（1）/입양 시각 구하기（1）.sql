-- 코드를 입력하세요
SELECT hour(datetime) 'hour', count(animal_id) 'count'
from animal_outs
where hour(datetime) between 9 and 19
group by 1
order by 1;