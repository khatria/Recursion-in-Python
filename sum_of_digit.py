"""
Python program to compute sum of digits of a number using recursion
"""
def sum_of_digit(num):
    sum = num % 10
    
    #Base Case
    if num < 10:
        return num
    
    #Recusrive Case
    sum += sum_of_digit(num//10)
    return sum

print(sum_of_digit(123456))