def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
                
print_items(10)

'''
Here as we can see ever time a loop is nested inside a loop the complexity of the program is going to increase by n^number of nested loops.
so the time completixy of this program is going to be O(n^3).
but we can simply write the complexity as O(n^2) no matter how many times the program is executing exponentially.
'''


def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
    # this loop runs O(n^2) times             
                
    for i in range(n):
        print(i)
    # this loop runs O(n) times   
                
print_items(10)

''' 
Here the first loop is having the time complexity of O(n^2) and second loop is O(n)
if we combine the total complexity of the function.
O(n^2) + O(n) = O(n^2 + n)
as the number n goes higher(eg. 1 lakh or 1 million) then the O(n^2) will be much higher and O(n) will be insignificant in this equation.
so we can drop the non-Dominant term in the time complexity O(n).
then the time complexity of this function is said to be O(n^2).
'''