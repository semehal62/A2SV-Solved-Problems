l1,l2 = list(map(int,input().split()))

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

ans = [0]*l1
count = 0

first = 0
second = 0

while first < l1 or second < l2:
    if first != 0 and  arr1[first] == arr1[first-1]:
        ans[first] = ans[first-1]
        first += 1 

    elif second < l2 and arr1[first] == arr2[second]:
        while second < l2 and arr1[first] == arr2[second] :
            count += 1
            second += 1
        ans[first] = count

    else:
        if  second < l2 and arr1[first] > arr2[second]:
            second += 1
        else:
            first += 1




    count = 0





print(sum(ans))
