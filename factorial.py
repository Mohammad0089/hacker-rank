def find_factorial(number:int):
    fact =1
    if(number < 0 or type(number) != int):
        print('invalid number')
        return -1
    for i in range(1,number+1):
        fact *= i
    return fact

print(find_factorial(5))