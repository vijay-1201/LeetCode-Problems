class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Set={}
        
        for index,value in enumerate(nums):
            diff=target-value
            if diff in Set:
                return [Set[diff],index]
            Set[value]=index
            
        
        
            
    
        
        
