length = int(input())
arr = list(map(int,input().split()))

arr.sort()

index = (len(arr) + 1)// 2

print(arr[index-1])
