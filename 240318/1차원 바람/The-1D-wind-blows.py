windDirection = ['L','R']

def checkTransferWind(dataList, adjDataList) :
    for i in range(len(dataList)) :
        if dataList[i] == adjDataList[i] :
            return True
    return False


def beltMove(dataList, direct) :
    if direct == 'R' :
        return dataList[1:] + [dataList[0]]
    else :
        return [dataList[-1]] + dataList[:-1]

#True,True 이런식으로 top, bot return
def AfterWindArr(arr,wind) :
    windRow = wind[0]
    direction = wind[1]
    reverseDirection = wind[1]
    if direction == 'L' :
        reverseDirection = 'R'
    else :
        reverseDirection = 'L'

    top = [False,reverseDirection,-1]
    bot = [False,reverseDirection,-1]

    #1.기존꺼 뒤짚기
    if direction == 'L' :
        arr[windRow] = beltMove(arr[windRow], "L")
    else :
        arr[windRow] = beltMove(arr[windRow], "R")
    #2.전파 체크
    #TOP CHECK
    if (windRow-1) >= 0 and checkTransferWind(arr[windRow], arr[windRow-1]) :
        top[0] = True
        top[2] = windRow-1
    #BOT CHECK 
    if (windRow+1) <= len(arr)-1 and checkTransferWind(arr[windRow], arr[windRow+1]) :
        bot[0] = True
        bot[2] = windRow+1
    
    return top,bot

n,m,q = map(int,(input().split()))
arr = []

for i in range(n) :
    arr.append(list(map(int,input().split())))

winds = []
for i in range(q) :
    data = input().split()
    data[0] = int(data[0]) - 1
    winds.append(data)

#wind에는 행과 방향이 있다~
for wind in winds :
    top,bot = AfterWindArr(arr,wind)
    topStart = top[0]
    botStart = bot[0]
    topWind = [top[2],top[1]]
    botWind = [bot[2],bot[1]]

    #top 전파시작
    while topStart :
        transferWind,_ = AfterWindArr(arr,topWind)
        topStart = transferWind[0]
        topWind = [transferWind[2],transferWind[1]]

    while botStart : 
        _,transferWind = AfterWindArr(arr,botWind)
        botStart = transferWind[0]
        botWind = [transferWind[2],transferWind[1]]





for i in range(len(arr)) :
    for j in range(len(arr[i])) :
        print(arr[i][j], end = ' ')
    print()