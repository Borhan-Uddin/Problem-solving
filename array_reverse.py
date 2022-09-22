
arr = [5,0,3,100]

start = 0
end = len(arr) - 1

while start < end:
    # temp = arr[start]
    # print(f"Pass {start}, Temp is :{temp}")
    # arr[start] = arr[end]
    # print(f"Pass {start}, arr[start] is :{arr[start]}")
    # arr[end] = temp
    # print(f"Pass {start}, arr[end] is :{arr[end]}")

    arr[start], arr[end]  = arr[end], arr[start]
    start+=1
    end-=1

for n in arr:
    print(n)
