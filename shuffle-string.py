class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = []
        for c1, c2 in zip(s,indices):
            arr.append((c2,c1))

        arr.sort()
        string = ""
        for i, w in arr:
            string += w

        return string
