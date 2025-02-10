-- 코드를 입력하세요
SELECT ingredient_type, SUM(total_order) total_order
FROM  first_half fh JOIN icecream_info ii ON fh.flavor = ii.flavor 
GROUP BY 1
ORDER BY 2;