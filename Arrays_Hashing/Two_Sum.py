

"""

Two Sum:

Given an array of integers nums and an integer target, return the indices 
i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j 
that satisfy the condition.

Return the answer with the smaller index first.

"""

class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)-1):
            for j in range(i+1,len(nums)):
                if (target-nums[i]== nums[j]):
                    return [i,j]

        return []
    
if __name__ == "__main__":
    input = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSumBruteForce(input, target))