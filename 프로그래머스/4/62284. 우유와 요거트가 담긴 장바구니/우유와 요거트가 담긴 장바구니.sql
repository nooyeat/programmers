-- 코드를 입력하세요
WITH 
t1 as (
    SELECT cart_id, group_concat(name) products
    FROM cart_products
    GROUP BY 1
    HAVING GROUP_CONCAT(NAME) LIKE '%MILK%' AND GROUP_CONCAT(NAME) LIKE '%YOGURT%'
)

SELECT cart_id
FROM T1;
  
    
