def add_numbers(n):
    return n+n+n 
    # complexity O(1)

add_numbers(30)

''' 
here in the add_number fucntion the time complexity will always remains O(1) no matter how large the n is.
because at the end the operation performed is still just one operation.
even if we adding n 3 or 4 times the time complexity will remain O(1).it will not increase to O(3) or O(4).
'''