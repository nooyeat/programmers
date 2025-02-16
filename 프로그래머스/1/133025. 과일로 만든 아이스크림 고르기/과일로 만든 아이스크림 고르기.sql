-- 코드를 입력하세요
SELECT distinct fh.flavor
FROM first_half fh
JOIN icecream_info ii on fh.flavor = ii.flavor
WHERE total_order >= 3000 and ingredient_type = 'fruit_based'
ORDER BY total_order desc;