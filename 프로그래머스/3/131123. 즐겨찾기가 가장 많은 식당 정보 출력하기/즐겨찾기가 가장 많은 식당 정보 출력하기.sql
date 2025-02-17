-- 코드를 입력하세요
SELECT food_type, rest_id, rest_name, favorites
FROM rest_info
WHERE favorites in (SELECT max(favorites)
                    FROM rest_info
                    GROUP BY food_type)
GROUP BY 1
ORDER BY 1 desc;