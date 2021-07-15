def factorial(n):
    #base case
    if n <= 0: #1
        return 1
    return n*factorial(n-1) #2

if __name__=="__main__":
    for i in range(1,6):
        print(factorial(i))
