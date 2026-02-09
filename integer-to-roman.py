class Solution:
    def intToRoman(self, num: int) -> str:
        dict1 = {1:"I", 5:"V", 10:"X" , 50:"L", 100:"C", 500:"D", 1000:"M"}
        roman = ""
        n = len(str(num))
        for i in str(num):
            if i == "4":
                if n == 3:
                    roman +=  dict1[100] + dict1[500] 
                elif n == 2:
                    roman +=  dict1[10] + dict1[50] 
                elif n == 1:
                    roman +=  dict1[1] + dict1[5] 
            elif i == "9":
                if n == 3:
                    roman +=  dict1[100] + dict1[1000] 
                elif n == 2:
                    roman +=  dict1[10] + dict1[100] 
                elif n == 1:
                    roman +=  dict1[1] + dict1[10]
            elif n == 4:
                roman += dict1[1000] *int(i)
            elif n == 3:
                div = int(i) // 5
                rem = int(i) % 5
                roman += div* dict1[500] + rem * dict1[100]
            elif n == 2:
                div = int(i) // 5
                rem = int(i) % 5
                roman += div* dict1[50] + rem * dict1[10]
            elif n == 1:
                div = int(i) // 5
                rem = int(i) % 5
                roman += div* dict1[5] + rem * dict1[1]

            n -= 1

        return roman
