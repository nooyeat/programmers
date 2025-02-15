-- 코드를 입력하세요
SELECT fd.product_id, product_name, sum(price*amount) total_sales
FROM food_product fd
JOIN food_order fo ON fd.product_id = fo.product_id
WHERE produce_date like '2022-05%'
GROUP BY 1
ORDER BY 3 DESC, 1;