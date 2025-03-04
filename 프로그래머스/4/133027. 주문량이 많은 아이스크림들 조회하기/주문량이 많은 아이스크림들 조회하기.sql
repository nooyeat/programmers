-- 코드를 입력하세요
SELECT fh.flavor
FROM first_half fh
JOIN july j on fh.flavor = j.flavor
GROUP BY 1
ORDER BY sum(fh.total_order) + sum(j.total_order) desc
LIMIT 3