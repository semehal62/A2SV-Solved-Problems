class Solution:
    def minMoves(self, target: int, mxd: int) -> int:

        # reduces target untill it becoms 1
        operation = 0
        while mxd and target != 1:
            if target % 2 == 0:
                target //=  2
                mxd -= 1
            else:
                target -= 1
            operation += 1
        

        return operation + target -1


       