num1 = int(input())
num2 = int(input())

def solveMeFirst(a,b):
    
    return (a + b) 
    # Hint: Type return a+b below

''' add a and b then return the result type int 
         1<=a , b<=1000 
    Decorator to do a range check '''

def rangeCheck(func):
    def calculate(a,b):
        if (a <= 1 or b <= 1):
            raise ValueError("numbers are below 1")
        elif(a >= 1000 or b >= 1000):
            raise ValueError("numbers are over the limit 1000")
        else:
            return func(a,b)
    return calculate        


#res = solveMeFirst(num1,num2)
res1 = rangeCheck(solveMeFirst)
total = res1(num1,num2)
print(total)