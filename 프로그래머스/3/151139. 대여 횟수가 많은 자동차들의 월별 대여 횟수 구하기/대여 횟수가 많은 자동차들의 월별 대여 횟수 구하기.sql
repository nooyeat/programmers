-- 코드를 입력하세요
SELECT month(start_date) month,
        car_id,
        count(car_id) records
FROM car_rental_company_rental_history
WHERE start_date between '2022-08-01' and '2022-10-31' 
AND car_id in (SELECT car_id
              FROM car_rental_company_rental_history
              WHERE start_date between '2022-08-01' and '2022-10-31' 
              GROUP BY 1
              HAVING count(car_id) >= 5)
GROUP BY 1, 2
ORDER BY 1, 2 desc;