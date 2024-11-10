-- 코드를 입력하세요
SELECT YEAR(os.sales_date) as YEAR,
MONTH(os.sales_date) as MONTH,
ui.gender,
count(distinct(os.user_id)) as USERS
from online_sale as os, user_info as ui
where ui.gender is not null and os.user_id=ui.user_id
group by 2,3
order by 1,2,3