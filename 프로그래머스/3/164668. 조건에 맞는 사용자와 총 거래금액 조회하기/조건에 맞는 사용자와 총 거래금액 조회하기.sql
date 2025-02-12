-- 코드를 입력하세요
SELECT user_id, nickname, sum(price)
FROM used_goods_board ugb JOIN used_goods_user ugu
ON ugb.writer_id = ugu.user_id
WHERE status = 'DONE'
GROUP BY 1, 2
HAVING sum(price) >= 700000
ORDER BY 3;