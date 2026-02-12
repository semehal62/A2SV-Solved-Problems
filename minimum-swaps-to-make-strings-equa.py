class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count_s1 = Counter(s1)
        count_s2 = Counter(s2)
        total_x ,total_y = 0,0

        total_x += count_s1["x"] + count_s2["x"]
        total_y += count_s1["y"] + count_s2["y"]

        if total_x % 2 != 0 or total_y % 2 != 0:
            return -1

        total_x /= 2
        total_y /= 2

        count_x = 0
        count_y = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    count_x += 1
                else:
                    count_y += 1

        ans = ceil(count_y / 2) + ceil(count_x/2)
        return ans

        
