-- 코드를 입력하세요
SELECT datetime
FROM animal_ins
WHERE datetime = (SELECT max(datetime)
                  FROM animal_ins)