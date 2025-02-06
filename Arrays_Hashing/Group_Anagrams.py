from typing import List
from collections import defaultdict

"""
Group Anagrams

Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order. 

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.
"""


class Solution:
    def groupAnagramsSorted(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
    
    def groupAnagramsHashTable(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print(sol.groupAnagramsSorted(strs))
    print(sol.groupAnagramsHashTable(strs))