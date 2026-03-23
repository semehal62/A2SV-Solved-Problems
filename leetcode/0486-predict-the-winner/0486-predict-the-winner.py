class Solution:

    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def winner(turn,alices, bob,nums):
            if not nums:
                return alices >= bob

            if turn:
                option1 =  winner(1-turn, alices + nums[0], bob,nums[1:]) 
                option2 =  winner(1-turn, alices + nums[-1], bob,nums[:len(nums)-1]) 
                return option1 or option2
            else:
                option1 =  winner(1-turn, alices, bob + nums[0],nums[1:]) 
                option2 =  winner(1-turn, alices, bob + nums[-1],nums[:len(nums)-1]) 
                return option1  and  option2

        return winner(1,0,0,nums)
                
                




