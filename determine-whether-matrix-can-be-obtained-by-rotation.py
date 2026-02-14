class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def Transpose(matrix):
            arr = copy.deepcopy(matrix)
            for i in range(len(arr)):
                for j in range(i+1,len(arr[i])):
                    arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
            

            return arr
        
        def reverse(matrix):
            arr = copy.deepcopy(matrix)
            for matrix in arr:
                matrix.reverse()


            return arr

            
        first = reverse(Transpose(mat))

        second = reverse(Transpose(first))

        thrid  = reverse(Transpose(second))


        if target == mat or target == first or target == second or target == thrid:
            return True
        else:
            return False

        
