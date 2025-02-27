-- 코드를 입력하세요
SELECT car_id,
        case when car_id in (SELECT car_id
                            FROM car_rental_company_rental_history
                            WHERE '2022-10-16' between start_date and end_date)
            then '대여중'
            else '대여 가능' end availability
FROM car_rental_company_rental_history
GROUP BY 1
ORDER BY 1 desc;