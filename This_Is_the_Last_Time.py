t = int(input())
def last():
    n, k = list(map(int,input().split()))
    collection = []
    for i in range(n):
        a,b,c = list(map(int,input().split()))
        collection.append((a,b,c))

    collection.sort(key=lambda x:(x[0],x[2]))

    stack = []
    stack.append(collection[0])

    for i in range(1, len(collection)):
        a,b,c = stack.pop()
        e,f,g = collection[i]

        if e <= c:
            stack.append((min(a,e),max(b,f),max(c,g)))
        else:
            stack.append((a,b,c))
            stack.append((e,f,g))

    stack.sort(key=lambda x: -x[2])
    for j in range(len(stack)):
        x,y,z = stack[j]
        if x <= k <= y  and z > k:
            k = z 
            break


        
    


    return k

for _ in range(t):
    print(last())
