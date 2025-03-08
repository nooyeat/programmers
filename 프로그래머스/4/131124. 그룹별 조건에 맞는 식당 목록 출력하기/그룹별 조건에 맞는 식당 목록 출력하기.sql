-- 코드를 입력하세요
SELECT member_name,
        review_text,
        date_format(review_date, '%Y-%m-%d') review_date
FROM member_profile mp
JOIN rest_review rr on mp.member_id = rr.member_id
WHERE rr.member_id in (SELECT member_id
                       FROM rest_review
                       GROUP BY 1
                       HAVING count(member_id) = (SELECT count(*)
                                                 FROM rest_review
                                                 GROUP BY member_id
                                                 ORDER BY 1 desc
                                                 LIMIT 1)
                       )
ORDER BY 3, 2