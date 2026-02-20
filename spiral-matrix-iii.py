class Solution:
    def right(self,curr_r,curr_c,add):
        result = []

        for i in range(add):
            result.append([curr_r,curr_c+i])

        return result

    def left(self,curr_r,curr_c,add):
        result = []

        for i in range(add):
            result.append([curr_r,curr_c-i])

        return result

    def up(self,curr_r,curr_c,add):
        result = []

        for i in range(add):
            result.append([curr_r-i, curr_c])

        return result

    def down(self,curr_r,curr_c,add):
        result = []

        for i in range(add):
            result.append([curr_r+i,curr_c])

        return result

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []

        up = False
        down = False
        right = True
        left = False

        add = 1
        total = rows * cols
        ans.append([rStart,cStart])
        cStart += 1
        while len(ans) < total:
            if right:
                retu = self.right(rStart,cStart,add)
                for a,b in retu:
                    if 0 <= a < rows and  0 <= b < cols:
                        ans.append([a,b])
                    rStart ,cStart = a+1,b
                right = False
                down = True
            
            if down:
                retu = self.down(rStart,cStart,add)
                for a,b in retu:
                    if 0 <= a < rows and  0 <= b < cols:
                        ans.append([a,b])
                    rStart ,cStart = a,b-1
                down = False
                left = True
          
            add += 1
            
            if left:
                retu = self.left(rStart,cStart,add)
                for a,b in retu:
                    if 0 <= a < rows and  0 <= b < cols:
                        ans.append([a,b])
                    rStart ,cStart = a-1,b
                left = False
                up = True

            if up:
                retu = self.up(rStart,cStart,add)
                for a,b in retu:
                    if 0 <= a < rows and  0 <= b < cols:
                        ans.append([a,b])
                    rStart ,cStart = a,b+1
                up = False
                right = True
           
            add += 1
           

           
          


            

        return ans

                
            
