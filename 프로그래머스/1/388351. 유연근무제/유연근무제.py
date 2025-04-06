def time_to_min(time_value):
    hour = time_value // 100
    minute = time_value % 100
    return hour * 60 + minute

def solution(schedules, timelogs, startday):
    answer = 0
    startday -= 1
    weekend = [5, 6]
    
    late_people = set()

    for i in range(7):
        today = (startday + i) % 7
        if today in weekend: 
            continue

        for j in range(len(schedules)):
            if time_to_min(timelogs[j][i]) > time_to_min(schedules[j]) + 10:
                late_people.add(j)

    return len(schedules) - len(late_people)