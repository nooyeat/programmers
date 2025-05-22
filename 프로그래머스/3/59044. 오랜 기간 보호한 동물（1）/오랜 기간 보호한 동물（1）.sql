-- 코드를 입력하세요
SELECT ai.name, ai.datetime
FROM animal_ins ai
LEFT JOIN animal_outs ao on ai.animal_id = ao.animal_id
WHERE ai.animal_id not in (SELECT animal_id
                          FROM animal_outs)
ORDER BY ai.datetime
LIMIT 3;