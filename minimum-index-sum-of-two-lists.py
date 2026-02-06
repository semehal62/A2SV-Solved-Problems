class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        set1 = set(list1)
        set2 = set(list2)
        set3  = set1 & set2
        length = len(set3)
        if length == 1:
            return list(set3)
        else:
            list3 = list(set3)
            word = []
            indexs  = 0 
            for s in list3:
                indexs += list1.index(s) + list2.index(s) 
                word.append((s,indexs))
                indexs = 0
            word.sort(key = lambda x:x[1])
        
        result = []
        x = word[0][1]
        for  w,i in word:
            if i == x:
                result.append(w)               


        return result 
        
