-- 코드를 입력하세요
SELECT ri.rest_id,
        rest_name,
        food_type,
        favorites,
        address,
        round(avg(review_score), 2) score
FROM rest_info ri 
JOIN rest_review rr on ri.rest_id = rr.rest_id
WHERE address like '서울%'
GROUP BY 1, 2
ORDER BY 6 desc, 4 desc;