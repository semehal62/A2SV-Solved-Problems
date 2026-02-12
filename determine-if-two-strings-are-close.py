class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count_1 = Counter(word1)
        count_2 = Counter(word2)


        if len(word1) != len(word2):
            return False

        if set(count_1.keys()) != set(count_2.keys()):
            return False
        
        if Counter(count_1.values()) == Counter(count_2.values()):
            return True
        else:
            return False
