def solution(today, terms, privacies):
    answer = []
    term_dict = {i: int(j) for i, j in (term.split(' ') for term in terms)}

    def add_month(str_date, months):
        year, month, day = map(int, str_date.split('.'))
        month += months
        year += (month-1) // 12
        month = (month-1) % 12 + 1
        day -= 1
        if day == 0:
            month -= 1
            if month == 0:
                year -= 1
                month = 12
            day = 28           
        return f'{year}.{month:02d}.{day:02d}'

    
    today_year, today_month, today_day = map(int, today.split('.'))

    for idx, privacie in enumerate(privacies, start=1):
        date, term = privacie.split(' ')
        expire_date = add_month(date, term_dict[term])
        year, month, day = map(int, expire_date.split('.'))
        if year < today_year or (year == today_year and month < today_month) or (year == today_year and month == today_month and day < today_day):
            answer.append(idx)
    return answer