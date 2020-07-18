"""
Program to convert a number to binary using recursion
"""

def find_binary(num):
    #Base Case
    if num == 0:
        return []
    
    #Recurisive Case
    binary_lst = find_binary(num//2)
    binary_lst.append(num%2)
    
    return binary_lst

print(find_binary(174))