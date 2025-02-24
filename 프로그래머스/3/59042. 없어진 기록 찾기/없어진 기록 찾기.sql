-- 코드를 입력하세요
SELECT ao.animal_id, ao.name
FROM animal_ins ai
RIGHT JOIN animal_outs ao on ai.animal_id = ao.animal_id
WHERE ai.animal_id is null
ORDER BY 1, 2