-- 코드를 입력하세요
SELECT a.apnt_no, p.pt_name, a.pt_no, a.mcdp_cd, dr_name, apnt_ymd
FROM patient p 
JOIN appointment a on p.pt_no = a.pt_no
JOIN doctor d on d.dr_id = a.mddr_id
WHERE date_format(apnt_ymd, '%Y-%m-%d') = '2022-04-13'
AND apnt_cncl_yn = 'n'
AND a.mcdp_cd = 'cs'
ORDER BY 5 desc;