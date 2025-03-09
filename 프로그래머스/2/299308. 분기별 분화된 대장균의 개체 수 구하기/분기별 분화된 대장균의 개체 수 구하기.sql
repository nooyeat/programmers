-- 코드를 작성해주세요
SELECT concat(quarter(differentiation_date), 'Q') quarter,
        count(id) ecoli_count
FROM ecoli_data
GROUP BY 1
ORDER BY 1;