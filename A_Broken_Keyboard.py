
from collections import Counter
t = int(input())

def correct():
    word = input()

    window = []
    left = 0
    correct = ""

    for right in range(len(word)):
        if word[right] in window:
            window += word[right]    
        else:
            if (len(window)) % 2 != 0:
                correct += "".join(window)
            while left != right:
                window.remove(word[left])
                left += 1
        
            window += word[right]  
        

    if (len(window)) % 2 != 0:
            correct += "".join(window)

    correct = sorted(set(correct))
    return "".join(correct)

for i in range(t):
    print(correct())
