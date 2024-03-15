n,t = map(int,input().split())
first = list(map(int,input().split()))
second = list(map(int,input().split()))
third = list(map(int,input().split()))

belt = first + second + third

def afterTsecondBelt(belt, t) :
    for _ in range(t) :
        belt = [belt[-1]] + belt[:3*n-1]
    
    for i in range(len(belt)) :
        if i >=n and i % n == 0 :
            print()
        print(belt[i], end = ' ')

afterTsecondBelt(belt,t)