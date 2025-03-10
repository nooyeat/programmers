-- 코드를 입력하세요
SELECT title,
        ugb.board_id,
        reply_id,
        ugr.writer_id,
        ugr.contents,
        date_format(ugr.created_date, '%Y-%m-%d') created_date
FROM used_goods_board ugb
JOIN used_goods_reply ugr on ugb.board_id = ugr.board_id
WHERE ugb.created_date like '2022-10%'
ORDER BY 6, 1;