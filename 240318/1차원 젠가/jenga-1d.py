n = int(input())
arr = []
for i in range(n) :
    arr.append(int(input()))

firstBlockStart, firstBlockEnd = map(int, input().split())
secondBlockStart, secondBlockEnd = map(int,input().split())

firstResultBlock = arr[:firstBlockStart-1] + arr[firstBlockEnd:]
secondResultBlock = firstResultBlock[:secondBlockStart-1] + firstResultBlock[secondBlockEnd:]

print(len(secondResultBlock))

for i in secondResultBlock :
    print(i)