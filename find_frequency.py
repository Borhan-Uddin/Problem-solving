arr = [1,1,1,2,2,3]
freq = dict()
k = 2
for n in arr:
    if n not in freq:
        freq[n] =1
    else:
        freq[n]+=1

print(1 in freq.keys())