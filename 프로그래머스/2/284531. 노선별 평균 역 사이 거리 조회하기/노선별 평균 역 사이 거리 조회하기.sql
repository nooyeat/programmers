-- 코드를 작성해주세요
SELECT route,
        concat(round(sum(d_between_dist), 1), 'km') total_distance,
        concat(round(avg(d_between_dist), 2), 'km') average_distance
FROM subway_distance
GROUP BY 1
ORDER BY sum(d_between_dist) desc;