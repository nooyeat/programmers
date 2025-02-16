-- 코드를 입력하세요
SELECT price div 10000 * 10000 AS price_group, count(product_id) products
FROM product
GROUP BY 1
ORDER BY 1;