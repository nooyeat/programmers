-- 코드를 작성해주세요
SELECT id, fish_name, length
FROM fish_info
JOIN fish_name_info on fish_info.fish_type = fish_name_info.fish_type
WHERE (fish_name, length) in (SELECT fish_name, max(length)
                              FROM fish_info fi
                              JOIN fish_name_info fni on fi.fish_type = fni.fish_type
                              GROUP BY fish_name
                             )
ORDER BY 1;