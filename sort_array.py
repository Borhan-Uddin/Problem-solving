arr = [777 ,83, 417, 746]#[5,0,-500,3,100,-100]

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] > arr[j]:
#             temp = arr[j]
#             arr[j] = arr[i]
#             arr[i] = temp

print(arr)

#using only one loop

i =1

while i < len(arr)-1:
    if arr[i] > arr[i+1]:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp

        i = -1
    i+=1

print(arr)