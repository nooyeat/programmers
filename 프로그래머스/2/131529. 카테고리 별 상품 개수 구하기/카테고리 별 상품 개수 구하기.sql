-- 코드를 입력하세요
SELECT left(product_code, 2) as category, count(*)
from product
group by 1
order by 1;