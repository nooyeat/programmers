def solution(price, money, count):
    total_price=0
    for i in range(1,count+1):
        
        price1=price*i
        print(price1)
        total_price=total_price+price1
    if total_price>money:
        return total_price-money
    else:
        return 0
    
