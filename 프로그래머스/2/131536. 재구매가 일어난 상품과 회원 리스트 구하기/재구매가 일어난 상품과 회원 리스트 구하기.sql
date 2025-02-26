-- 코드를 입력하세요
SELECT user_id, product_id
FROM online_sale
WHERE (user_id, product_id) in (SELECT distinct user_id, product_id
                               FROM (SELECT user_id, product_id, count(user_id) user_cnt
                                    FROM online_sale
                                    GROUP BY 1, 2) as count_sub
                               WHERE user_cnt > 1)
GROUP BY 1, 2
ORDER BY 1, 2 desc;