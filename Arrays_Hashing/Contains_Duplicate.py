from typing import List
from collections import defaultdict

"""
Contains Duplicate

Given an integer array nums, return true if any value appears 
more than once in the array, otherwise return false.

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if(nums[i]== nums[i-1]):
                return True

        return False  
        
         
    
if __name__ == "__main__":
    input = [1, 2, 3, 3]
    sol = Solution()
    print(sol.groupAnagramsSorted(input))
    print(sol.groupAnagramsHashTable(input))