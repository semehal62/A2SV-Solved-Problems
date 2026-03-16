class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # bills.sort()/
        change = defaultdict(int)

        for i in range(len(bills)):
            
            if bills[i] == 10 and change[5] > 0:
                change[5] -= 1
            elif bills[i] == 10 and change[5] <= 0:
                return False

           
            if bills[i] == 20 and change[5] > 0 and change[10] > 0:
                change[5] -= 1
                change[10] -= 1
            elif bills[i] == 20 and change[5] >= 3:
                change[5] -= 3
            elif bills[i] == 20 and (change[5] <= 0 or change[10] <= 0):
                return False

            change[bills[i]] += 1

        return True