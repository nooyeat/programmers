-- 코드를 작성해주세요
SELECT distinct he.emp_no,
        emp_name,
        case when avg(score) >= 96 then 'S'
            when avg(score) >= 90 then 'A'
            when avg(score) >= 80 then 'B'
            else 'C' end grade,
        case when avg(score) >= 96 then sal*0.2
            when avg(score) >= 90 then sal*0.15
            when avg(score) >= 80 then sal*0.1
            else 0 end bonus
FROM hr_employees he
JOIN hr_grade hg on he.emp_no = hg.emp_no
GROUP BY 1
ORDER BY 1;