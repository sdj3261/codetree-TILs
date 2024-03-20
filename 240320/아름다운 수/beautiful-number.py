global cnt 
nums = ['1','2','3','4']
def is_beautiful(s):
    i = 0
    while i < len(s) :
        length = int(s[i])
        if s[i:i+length] != s[i] * length :
            return False
        else :
            i = i+length 
    return True

def generateNumberNdigit(s,n) :
    if n==0 :
        if is_beautiful(s) :
            global cnt
            cnt += 1
            return
        return
    for i in nums:
        s+=i
        generateNumberNdigit(s,n-1)
        s = s[:-1]


#n은 자릿수
n = int(input())
cnt = 0
s = ""
generateNumberNdigit(s,n)
print(cnt)