-- 코드를 입력하세요
SELECT ai.animal_id, ai.animal_type, ai.name
FROM animal_ins ai 
JOIN animal_outs ao ON ai.animal_id = ao.animal_id
WHERE sex_upon_intake like 'intact%' 
AND (sex_upon_outcome like 'spayed%' or sex_upon_outcome like 'neutered%');