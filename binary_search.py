
arr = [1,2,5,6,10]

k = 5
start = 0
end = len(arr) - 1
mid = int((start+end)/2 )

print(mid)
while start <= end:
    if k > arr[mid]:
        start = mid +1
        mid = int ((start + end)/2)
    elif k == arr[mid]:
        pos = mid
    elif k < arr[mid]:
        end = mid -1
        mid = int ((start + end)/2)
    

print(pos)
