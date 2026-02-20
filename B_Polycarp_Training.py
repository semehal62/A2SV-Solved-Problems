length = int(input())
arr = list(map(int,input().split()))


arr.sort()

count = 0
days = 1
for i in range(len(arr)):
    if arr[i] >= days:
        count += 1
        days += 1

print(count)
