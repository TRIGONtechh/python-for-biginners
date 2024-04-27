# docstrings takes the output wch is add inside '''x''' wch can be used by __doc__ 
# doc is taken when doc is nect line of the def 


def square(n):
    '''Takes the square of element'''
    print(n**2)

square(5)
print("\n")
print(square(6))
print(square.__doc__)
