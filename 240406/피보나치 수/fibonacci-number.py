def fibo(n) :
    if n == 1 :
        return 1
    elif n == 2 :
        return 1
    else :
        return fibo(n-2) + fibo(n-1)
a = int(input())
print(fibo(a))