-- 코드를 작성해주세요
SELECT count(id) fish_count, fish_name
FROM fish_info fi 
JOIN fish_name_info fni on fi.fish_type = fni.fish_type
GROUP BY fi.fish_type, fish_name
ORDER BY 1 desc;