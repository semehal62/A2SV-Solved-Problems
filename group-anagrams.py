class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            anagrams[tuple(sorted(i))].append(i)

        coll = []
        for val in anagrams.values():
            coll.append(val)
        return coll
