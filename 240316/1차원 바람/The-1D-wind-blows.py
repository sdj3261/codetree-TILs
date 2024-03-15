windDirection = ['L','R']

def checkTransferWind(dataList, adjDataList) :
    for i in range(len(dataList)) :
        if dataList[i] == adjDataList[i] :
            return True
    return False


def DirectionBelt(dataList, direct) :
    if direct == 'R' :
        return dataList[-1] + dataList[0:len(dataList)-1]
    else :
        return dataList[1:len(datList)-1] + dataList[0]

def AfterWindArr(arr,wind) :
    windRow = wind[0]
    windTopRow = windRow
    windBotRow = windRow
    direction = wind[1]

    #바람불기
    #top 방향 진행 조건
    while windTopRow >= 0 or checkTransferWind(arr[windRow],arr[windRow-1])
    #bottom 방향
    

n,m,q = map(int,(input().split()))
arr = []

for i in range(n) :
    arr.append(map(int,input().split()))

wind = []
for i in q :
    data = input().split()
    data[0] = int(data[0]) - 1
    wind.append(data)