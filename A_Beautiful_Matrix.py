matrix = []
colunm = 0
row = 0
for i in range(5):
    col = list(map(int,input().split()))  
    if 1 in col:
        row = i +1
        for c in range(len(col)):
            if col[c] == 1:
                colunm = c + 1
                break

count = abs(3-row) + abs(3-colunm)

print(count)



