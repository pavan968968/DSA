from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1  # child satisfied
            j += 1     # move cookie pointer
        return i
