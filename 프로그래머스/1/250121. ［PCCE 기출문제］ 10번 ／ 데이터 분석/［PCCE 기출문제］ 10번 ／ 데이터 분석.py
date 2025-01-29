def solution(data, ext, val_ext, sort_by):
    answer = []
    code_dict = {'code':0, 'date':1, 'maximum':2, 'remain':3}

    for key,val in code_dict.items():
        if ext == key:
            ext = val
        if sort_by == key:
            sort_by=val
    
    col_val = [row[ext] for row in data]       
    for val in col_val:
        if val < val_ext:
            answer.append(data[col_val.index(val)])
    answer.sort(key=lambda x:x[sort_by])
        
    return answer