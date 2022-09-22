
arr1 = [1,2,3,4,0,0]
arr2 = [1,0,3,0,2,4]

#print(arr1 == arr2)

# flag = False
# for n in arr1:
#     if n in arr2:
#         flag = True

def count_digits(arr):
    freq = {}

    for n in arr:
        if n not in freq:
            freq[n] =1
        else:
            freq[n]+=1
    return freq

print(count_digits(arr1) == count_digits(arr2))
print(count_digits(arr2))
