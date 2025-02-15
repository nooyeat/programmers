-- 코드를 입력하세요
SELECT category, price, product_name
FROM food_product
WHERE price in (SELECT max(price)
                FROM food_product
                GROUP BY category)
AND category in ('과자', '국', '김치', '식용유')
GROUP BY 1
ORDER BY 2 DESC;