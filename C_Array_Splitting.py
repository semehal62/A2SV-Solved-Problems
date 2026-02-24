
n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))

ans = []

arr.sort()

for i in range(1,n):
    ans.append(arr[i]-arr[i-1])

ans.sort()
res = sum(ans)
for i in range(len(ans) - 1, len(ans) - k, -1):
    res -= ans[i]
print(res)
