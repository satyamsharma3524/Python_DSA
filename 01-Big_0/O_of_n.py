def print_items(n):
    for i in range(n):
        print(i)
        
    print("\n\n")
        
print_items(10)


'''
this upper code is gonna run in the time complexity of O(n).
because the number of operation performed is proportional to n.
'''


def print_items(n):
    for i in range(n):
        print(i)
        
    for J in range(n):
        print(J)
        
print_items(10)


'''
this upper code is gonna run in the time complexity of O(2n). because the number of operation performed is proportional to 2 times n.
but we can drop the constant factor 2 and simply write the complexity as O(n).
'''