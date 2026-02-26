length, target = list(map(int,input().split()))
nums = list(map(int,input().split()))

left = 0
sums = 0
count = 0

for right in range(length):
    sums += nums[right]
    while sums - nums[left] >= target:
        sums -= nums[left]
        left += 1
    if sums >= target:
        count += left + 1
    

print(count)
