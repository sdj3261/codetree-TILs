def shift(a) :
    return a[-1] + a[0:len(a)-1]
def run(a) :
    cnt = 1
    ret = ""
    encodeChar = a[0]
    for i in range(1,len(a)) :
        if encodeChar == a[i] :
            cnt += 1
        else :
            encodeChar = encodeChar + str(cnt)
            ret = ret + encodeChar
            cnt = 1
            encodeChar = a[i]
    if cnt > 0 :
        encodeChar = encodeChar + str(cnt)
        ret = ret + encodeChar
    return len(ret)
            

a = input()
n = len(a) - 1
minEncode = 1000
if len(a) == 1 :
    print(2)
else :
    for i in range(n) :
        a = shift(a)
        encode = run(a)
        minEncode = min(minEncode,encode)
    print(minEncode)