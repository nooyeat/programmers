-- 코드를 입력하세요
SELECT year(sales_date) year,
        month(sales_date) month,
        gender,
        count(distinct ui.user_id) user_id
FROM user_info ui
JOIN online_sale os on ui.user_id = os.user_id
WHERE gender is not null
GROUP BY 1, 2, 3
ORDER BY 1, 2, 3