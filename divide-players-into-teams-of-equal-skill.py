class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left,right = 0,len(skill) - 1
        equal = skill[left] + skill[right]
        product = 1
        chemistry = 0
        while left <= right:
            if  skill[left] + skill[right] != equal:
                return -1
            else:
                product =  skill[left] * skill[right]
                chemistry += product
                left += 1
                right -= 1

        return chemistry 
