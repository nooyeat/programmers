-- 코드를 입력하세요
SELECT mcdp_cd '진료과 코드', count(apnt_no) '5월예약건수'
from appointment
where apnt_ymd like '2022-05%'
group by 1
order by 2, 1;