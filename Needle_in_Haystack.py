from collections import Counter
t = int(input())

def subseq():
    s = input()
    t = input()
    count_s = Counter(s)
    count_t = Counter(t)



    s = list(s)
    for key, value in count_s.items():
        if key not in count_t  or  value > count_t[key]:
            return "Impossible"
        else:
            count_t[key] -= value
            if count_t[key] == 0:
                del count_t[key]
    i = 0

    for k,v in count_t.items():
        i = 0

        while  i <= len(s)-1 and  k >= s[i]:
        
            i += 1
        else:
            add = v*k
            v = 0
            s.insert(i,add)

            
    return "".join(s)



for _ in range(t):
    print(subseq())
