class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dict1 = defaultdict(list)
        ans = []

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                dict1[i+j].append((i,j))

        length = len(mat)
        mid = ceil(len(dict1)/2) -1
        count = 0

        for key, val in dict1.items():
            if key % 2 == 0:
               val.sort(key = lambda x:-x[0])
            else:
                val.sort()

            for k in val:
                    ans.append( mat[int(k[0])][int(k[1])] )

            

                


        return ans
