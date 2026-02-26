length, target = list(map(int,input().split()))
nums = list(map(int,input().split()))

left = 0
sums = 0
count = 0
for right in range(len(nums)):
    sums += nums[right]
    while sums > target:
        sums -= nums[left]
        left += 1
    count += right -left + 1

print(count)
