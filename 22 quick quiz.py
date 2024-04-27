# def fibonacci(n):
#     a, b = 0, 1
#     count = 0
#     while count < n:
#         print(a, end=' ')
#         a, b = b, a + b
#         count += 1
#     print(count)

# # Example: Generate the first 10 Fibonacci numbers
# fibonacci(10)

def fibonacci(n):
    a = 0
    b = 1
    fab = 0
    while fab < n:
        print(a)
        a,b = b , a+b
        fab += 1
    print(fab)

fibonacci(10)

# 0,1 = 1 , 1 
# 1,1 = 1,2
# 1,2 = 2,3
# 3,4 = 4,7 


