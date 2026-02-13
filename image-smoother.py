class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        dire_top = [(-1,-1),(-1,0),(-1,1)]
        dire_mid =  [(0,-1),(0,0),(0,1)]
        dire_buttom =  [(1,-1),(1,0),(1,1)]

        top, mid, buttom = 0,0,0 
        c_t,c_m,c_b = 0,0,0   

        arr = copy.deepcopy(img)

        for i in range(len(img)):
            for j in range(len(img[i])):
                x,y = i,j
                for a,b in dire_top:
                    new_i = i + a
                    new_j = j + b
                    
                    if 0 <= new_j < len(img[0]) and 0 <= new_i < len(img):
                        top += img[new_i][new_j]
                        c_t += 1
            

                for c,d  in dire_mid:
                    new_i = i + c
                    new_j = j + d

                    if 0 <= new_j < len(img[0]) and 0 <= new_i < len(img):
                        mid += img[new_i][new_j]
                        c_m += 1
                

                for e,f  in dire_buttom:
                    new_i = i + e
                    new_j = j + f

                    if 0 <= new_j < len(img[0]) and 0 <= new_i < len(img):
                        buttom += img[new_i][new_j]
                        c_b += 1
                
                cells = c_t + c_m + c_b
                arr[x][y] = (top + mid + buttom) // cells if cells != 0 else 0

                top, mid, buttom = 0, 0, 0 
                c_t, c_m, c_b = 0, 0, 0   

        return arr
