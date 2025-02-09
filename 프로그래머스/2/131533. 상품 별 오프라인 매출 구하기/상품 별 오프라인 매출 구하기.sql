-- 코드를 입력하세요
SELECT product_code, sum(price*sales_amount) sales
from product p 
join offline_sale os on p.product_id = os.product_id
group by 1
order by 2 desc, 1;