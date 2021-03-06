
print("Enter two or more positive numbers to calculate then press any non digit value or Enter to quit.")

numbers = list() # a list to hold the numbers

num = input()
while num.isdigit():     # getting numbers from user  # isdigit() returns false for numbers < 0
        numbers.append(int(num))    #adding the number to our list
        num = input()


''' all numbers sould be bigger than 0 and less than 1000
    def a decorator to check  the range'''

def checkRange(func): 
    def checker(listA):              # checker gets a list 
        for val in listA:
            if val > 1000:
                raise ValueError("Value over 1000 is not allowed")
            elif val < 1:
                raise ValueError('value less than 1 is not allowed')
        return func(listA)
    return checker

@checkRange
def adder(numbers):
    sum =0
    for val in numbers:
        sum +=val
    return sum

result = adder(numbers)
print(result)
