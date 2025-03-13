-- 코드를 입력하세요
WITH recursive 
num as (SELECT 0 as n
       UNION ALL
       SELECT n + 1 
       FROM num
       WHERE n < 23
)

SELECT n hour, count(animal_id) 'count'
FROM num
LEFT JOIN animal_outs ao on n = hour(datetime)
GROUP BY 1
ORDER BY 1;