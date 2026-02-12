class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict1 = Counter(ransomNote)
        dicts2 = Counter(magazine)
        print(dict1, dicts2)
        for key, value in dict1.items():
            if key not in dicts2 or value > dicts2[key]:
                return False
        return True 

