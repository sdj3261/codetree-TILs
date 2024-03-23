n,m = map(int,input().split())
arr = []

def combi(n,m,cnt,idx) :
    if cnt == m :
        print(*arr)
        return
    for i in range(idx,n+1) :
        arr.append(i)
        combi(n,m,cnt+1,i+1)
        arr.pop()
    

combi(3,2,0,1)