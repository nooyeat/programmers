-- 코드를 작성해주세요
SELECT distinct id, email, first_name, last_name
FROM developers d
JOIN skillcodes s on name in ('c#', 'python')
WHERE skill_code & `code` = `code`
ORDER BY 1;