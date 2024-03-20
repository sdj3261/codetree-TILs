global cnt 
def is_beautiful(arr):
    s = ""
    for i in arr :
        s+=str(i)
    i = 0
    while i < len(s) :
        length = int(s[i])
        if s[i:i+length] == s[i] * length :
            i = i+length
            pass
        else :
            return False
    return True

def generateNumberNdigit(arr,n) :
    if n==0 :
        if is_beautiful(arr) :
            global cnt
            cnt += 1
            return
        else :
            return
    for i in range(1, 5):
        arr.append(i)
        generateNumberNdigit(arr,n-1)
        arr.pop()


#n은 자릿수
n = int(input())
cnt = 0
arr = []
generateNumberNdigit(arr,n)
print(cnt)