-- 코드를 입력하세요
SELECT concat('/home/grep/src/', ugf.board_id, '/', file_id, file_name, file_ext) file_path
FROM used_goods_board ugb
JOIN used_goods_file ugf ON ugb.board_id = ugf.board_id
WHERE views = (SELECT max(views) 
              FROM used_goods_board)
ORDER BY file_id desc;