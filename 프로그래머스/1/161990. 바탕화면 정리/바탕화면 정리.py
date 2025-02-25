import re
def solution(wallpaper):
    new_wallpaper = []
    answer = [0, 0, 0, 0]
    x_idx = []
    y_idx = []

    for i in range(len(wallpaper)):
        new_wallpaper.append(wallpaper[i:i+1])

    for i in range(len(new_wallpaper)):
        str_paper = re.sub(r'[^.#]', '', str(new_wallpaper[i]))
        for j in range(len(str_paper)):
            if str_paper[j] == '#':
                x_idx.append(j)
        if '#' in str_paper:
            y_idx.append(i)
    answer[0] = min(y_idx)
    answer[1] = min(x_idx)
    answer[2] = max(y_idx) + 1
    answer[3] = max(x_idx) + 1
    return answer