t = int(input())
 
def dominat():
    # accepting input
    length = int(input())
    string = input()
    

    if len(string) < 2:
        return -1
    
    if "aa" in string:
        return 2
    elif "aca" in string or "aba" in string:
        return 3
    elif "abca" in string or "acba" in string:
        return 4
    elif "abbacca" in string or "accabba" in string:
        return 7
    else:
        return -1
 
 
 
for _ in range(t):
    print(dominat())
