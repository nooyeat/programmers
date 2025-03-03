-- 코드를 입력하세요
SELECT a.author_id, 
        a.author_name, 
        category, 
        sum(price * sales) total_sales
FROM book b
JOIN author a on b.author_id = a.author_id
JOIN book_sales bs on b.book_id = bs.book_id
WHERE sales_date like '2022-01%'
GROUP BY 1, 2, 3
ORDER BY 1, 3 desc;