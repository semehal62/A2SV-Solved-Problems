t = int(input())
def robot():
    l,x,s = list(map(int,input().split()))
    directions = input()
    prefix = []
    sums = 0
    for i in directions:
        if i == "L":
            sums -= 1
        else:
            sums += 1
        prefix.append(sums)
    count = 0
    
    if -x in prefix:
        index = prefix.index(-x) +1
        count += 1
        s -= index 
        if s > 0:
            if 0 in prefix:
                second_zero = prefix.index(0) + 1
                count += (s//second_zero)
                
            else:
                return count
    else:
        return 0
    
    return count
    0
for _ in range(t):
    print(robot())
