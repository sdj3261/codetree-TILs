n, m = map(int, input().split())
arr = []

for i in range(n) :
    arr.append(list(map(int,input().split())))
ret = -1

def is_rectangle(start_y,start_x) :
    min_width = 100000
    max_rect = -1000
    for i in range(start_y,n) :
        width = 0
        while start_x + width < m and arr[i][start_x+width] > 0 :
            width += 1
        min_width = min(min_width,width)
        rt = min_width * (i-start_y + 1)
        max_rect = max(max_rect,rt)
    return max_rect 
             
        

for i in range(n) :
    for j in range(m) :
        if arr[i][j] > 0 :
            max_sq_size = is_rectangle(i,j)
            ret = max(max_sq_size,ret)
print(ret)