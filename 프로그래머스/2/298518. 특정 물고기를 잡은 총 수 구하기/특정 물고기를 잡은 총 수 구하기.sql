-- 코드를 작성해주세요
SELECT count(fi.fish_type) fish_count
FROM fish_info fi
JOIN fish_name_info fni on fi.fish_type = fni.fish_type
WHERE fish_name = 'bass' or fish_name = 'snapper';