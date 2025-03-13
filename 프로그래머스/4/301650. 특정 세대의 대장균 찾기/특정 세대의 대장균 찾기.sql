-- 코드를 작성해주세요
WITH
first_gen as (
    SELECT id, parent_id
    FROM ecoli_data
    WHERE parent_id is null
),

second_gen as (
    SELECT ed.id, ed.parent_id
    FROM first_gen fg
    JOIN ecoli_data ed on fg.id = ed.parent_id
)

SELECT ed.id 
FROM second_gen sg
JOIN ecoli_data ed on sg.id = ed.parent_id
ORDER BY 1;