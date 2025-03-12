-- 코드를 입력하세요
SELECT date_format(sales_date, '%Y-%m-%d') sales_date,
        product_id,
        user_id,
        sum(sales_amount) sales_amount
FROM (SELECT online_sale_id, product_id, sales_amount, sales_date, user_id
     FROM online_sale
     UNION ALL
     SELECT *, NULL as user_id
     FROM offline_sale) as t
WHERE sales_date like '2022-03%'
GROUP BY 1, 2, 3
ORDER BY 1, 2, 3;