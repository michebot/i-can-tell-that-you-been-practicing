def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b

    # recursively
    # if n<0: 
    #     print("Incorrect input") 
    # # First fibonacci number is 0 
    # elif n==1: 
    #     return 0
    # # Second fibonacci number is 1 
    # elif n==2: 
    #     return 1
    # else: 
    #     return fibonacci(n-1)+fibonacci(n-2) 


print(fibonacci(9))