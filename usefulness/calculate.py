def calculate(num):
    if num == 0:
        return 0
    
    if num % 2 == 1:
        num -= 1
        
    return num + calculate(num - 2)

sum = calculate(7)
print (sum)