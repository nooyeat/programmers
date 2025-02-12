-- 코드를 입력하세요
SELECT distinct cc.car_id
FROM car_rental_company_car cc JOIN car_rental_company_rental_history rh
ON cc.car_id = rh.car_id
WHERE car_type = '세단' 
AND cc.car_id in (SELECT car_id 
                 FROM car_rental_company_rental_history
                 WHERE month(start_date) = 10)
ORDER BY 1 desc;