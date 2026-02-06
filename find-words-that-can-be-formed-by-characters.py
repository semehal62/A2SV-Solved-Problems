class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars = Counter(chars)
        length = 0
        for word in words:
            lens = len(word)
            word = Counter(word)
            for key, value in word.items():
                if key not in chars or chars[key] < value:
                    print(word)
                    break
            else:   
                length += lens

        return length
