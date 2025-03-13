-- 코드를 작성해주세요
SELECT id, 
        case when percent_rank() over(order by size_of_colony desc) <= 0.25 then 'CRITICAL'
            when percent_rank() over(order by size_of_colony desc) <= 0.5 then 'HIGH'
            when percent_rank() over(order by size_of_colony desc) <= 0.75 then 'MEDIUM'
            else 'LOW' end colony_name
FROM ecoli_data
ORDER BY 1;