-- 코드를 입력하세요
SELECT user_id, nickname, concat(city, ' ', street_address1, ' ', street_address2) 전체주소,
        concat_ws('-', left(tlno, 3), substr(tlno, 4, 4), right(tlno, 4)) 전화번호
FROM used_goods_board ugb
JOIN used_goods_user ugu on ugb.writer_id = ugu.user_id
GROUP BY 1
HAVING count(ugb.writer_id) >= 3
ORDER BY 1 desc;