class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = sorted(s)
        n = sorted(t)
        if m == n:
            return True
        else:
            return False
        