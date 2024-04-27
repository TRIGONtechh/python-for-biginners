# recurstion is a funtion wch call it itself 

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
  
    
print(factorial(4))

# so here print(factorial (4))
# so here print(factorial(3))
# so here print(factorial(2))
# so here print(factorial(1))
# like this all of the factorial is multiplied
# 4*3*2*1

