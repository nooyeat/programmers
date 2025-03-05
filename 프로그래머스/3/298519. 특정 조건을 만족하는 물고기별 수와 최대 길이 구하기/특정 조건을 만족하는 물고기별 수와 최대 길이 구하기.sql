-- 코드를 작성해주세요
WITH 
t1 as (
    SELECT id, 
            fish_type,
            case when length is null then 10
                else length end length
    FROM fish_info
)

SELECT count(id) fish_count,
        max(length) max_length,
        fish_type
FROM t1
GROUP BY 3
HAVING avg(length) >= 33
ORDER BY 3;