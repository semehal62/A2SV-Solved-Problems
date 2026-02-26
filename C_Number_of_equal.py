from collections import Counter
l1,l2 = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
 
c_arr1 = Counter(arr1)
c_arr2 = Counter(arr2)
count = 0
for key, value in c_arr1.items():
    if key in c_arr2:
        count += (value * c_arr2[key])
 
print(count)
