-- 코드를 입력하세요
SELECT round(avg(daily_fee)) average_fee
FROM car_rental_company_car
WHERE car_type = 'suv';