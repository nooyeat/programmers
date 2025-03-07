-- 코드를 작성해주세요
SELECT id,
        (SELECT count(parent_id)
        FROM ecoli_data AS a
        WHERE a.parent_id = ed.id) child_count
FROM ecoli_data ed
ORDER BY 1;