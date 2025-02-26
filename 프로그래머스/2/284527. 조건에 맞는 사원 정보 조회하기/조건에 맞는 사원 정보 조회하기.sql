-- 코드를 작성해주세요
SELECT sum(score) score, he.emp_no, emp_name, position, email
FROM hr_employees he
JOIN hr_grade hg ON he.emp_no = hg.emp_no
WHERE year = 2022
GROUP BY 2, 3, 4, 5
HAVING sum(score) = (SELECT max(sum_score)
                    FROM (SELECT emp_no, sum(score) sum_score
                         FROM hr_grade
                         WHERE year = 2022
                         GROUP BY 1) as sub) 