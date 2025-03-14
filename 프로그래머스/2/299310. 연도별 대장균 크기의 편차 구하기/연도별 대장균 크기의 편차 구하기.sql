-- 코드를 작성해주세요
WITH 
t1 as (SELECT year(differentiation_date) year, max(size_of_colony) size
      FROM ecoli_data
      GROUP BY 1
)

SELECT year, max(size - size_of_colony) year_dev, id
FROM t1
JOIN ecoli_data ed on year = year(differentiation_date)
group by 1, 3
ORDER BY 1, 2;