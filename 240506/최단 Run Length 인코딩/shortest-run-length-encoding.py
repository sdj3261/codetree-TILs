n = input()
k = len(n)

def runLengthEncoding(n) :
    d = dict()
    ret = ""
    newNum = n[-1] + n[:len(n)-1]
    for data in newNum :
        if data in d :
            d[data] += 1
        else :
            d[data] = 1
    for k,v in d.items() :
        ret += k
        ret += str(v)
    
    return len(ret)
        


ret = 1000
if k == 1 :
    print(2)
else :
    for i in range(len(n)-1) :
        ret = min(ret,runLengthEncoding(n))
    print(ret)

#shift 함수
#run-length encoding