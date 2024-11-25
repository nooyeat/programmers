def solution(sizes):
    max_wid=max_hei=0
    for size in sizes:
        width,height=size
        max_wid=max(max_wid, height, width)
        max_hei=max(max_hei, min(height, width))
    
    return  max_wid*max_hei

