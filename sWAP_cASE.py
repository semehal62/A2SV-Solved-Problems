def swap_case(s):
    ans = ""
    for i in s:
        if i.islower():
            ans += i.upper()
        else:
            ans += i.lower()
    return ans

if __name__ == '__main__':
