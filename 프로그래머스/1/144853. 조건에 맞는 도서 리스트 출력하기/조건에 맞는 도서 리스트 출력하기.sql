-- 코드를 입력하세요
SELECT book_id, date_format(published_date, '%Y-%m-%d') published_date
FROM book
WHERE published_date like '2021%' and category = '인문'
ORDER BY 2;