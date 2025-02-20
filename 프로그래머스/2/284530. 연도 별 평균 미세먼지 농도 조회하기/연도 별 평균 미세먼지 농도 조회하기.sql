-- 코드를 작성해주세요
SELECT year(ym) year, round(avg(pm_val1), 2) pm10, round(avg(pm_val2), 2) 'pm2.5'
FROM air_pollution
WHERE location2 = '수원'
GROUP BY 1
ORDER BY 1;