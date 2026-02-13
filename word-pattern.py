class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strings = s.split()
        

        word_to_pattern = defaultdict(str)
        pattern_to_word = defaultdict(str)

        if len(strings) != len(pattern):
            return False

        for p in range(len(pattern)):
            if pattern[p] not in word_to_pattern:
                word_to_pattern[pattern[p]] = strings[p]
            elif pattern[p] in word_to_pattern and word_to_pattern[pattern[p]] == strings[p]:
                pass
            else:
                return False

            if strings[p] not in pattern_to_word:
                pattern_to_word[strings[p]] = pattern[p]
            elif strings[p] in pattern_to_word and pattern_to_word[strings[p]] == pattern[p]:
                pass
            else:
                return False


        

        for key,val in word_to_pattern.items():
            if val not in pattern_to_word or  key != pattern_to_word[val]:
                return False

        print(word_to_pattern,pattern_to_word)

        for k,v in pattern_to_word.items():
            if v not in word_to_pattern or k !=  word_to_pattern[v]:
                return False

        
        return True
