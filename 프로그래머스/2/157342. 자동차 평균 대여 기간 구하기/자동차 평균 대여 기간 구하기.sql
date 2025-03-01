-- 코드를 입력하세요
SELECT car_id, round(avg(datediff(end_date, start_date) + 1), 1) average_duration
FROM car_rental_company_rental_history
GROUP BY 1
HAVING avg(datediff(end_date, start_date) + 1) >= 7
ORDER BY 2 desc, 1 desc;