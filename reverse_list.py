'''
Program to reverse a list using recursion
'''
def reverse_list(lst, a):
    #Base Case
    if a ==len(lst):
        return []
    
    #Recursive Case
    new_lst = reverse_list(lst, a + 1)
    new_lst.append(lst[a])

    return new_lst

print(reverse_list([1, 2, 3, 4], 0))