-- 코드를 작성해주세요
SELECT concat(length, 'cm') max_length
FROM fish_info
ORDER BY length desc
LIMIT 1;