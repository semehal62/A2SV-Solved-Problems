class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        comment = False
        temp = ""
        arr = []
        for string in source:
            s = 0
            while s < len(string):
                if string[s:s+2] == "//" and not comment:
                    break
                elif string[s:s+2] == "/*"  and  not comment:
                    comment = True 
                    s += 2
                elif  string[s:s+2] == "*/" and comment:
                    s += 2
                    comment = False 
                else:
                    if  not comment:
                        temp += string[s]
                    s += 1

            if not comment and temp:
                arr.append(temp)
                temp = ""

    
        return arr





