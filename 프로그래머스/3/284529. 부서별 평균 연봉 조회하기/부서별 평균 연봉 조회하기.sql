-- 코드를 작성해주세요
SELECT hd.dept_id, dept_name_en, round(avg(sal)) avg_sal
FROM hr_department hd
JOIN hr_employees he on hd.dept_id = he.dept_id
GROUP BY 1
ORDER BY 3 desc;