class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        j = len(needle)
        my_lis = []
        for i in range(len(haystack)):
            if (haystack[i:j] == needle):
                my_lis.append(i)
            j+=1
        if len(my_lis) != 0:
            return min(my_lis)
        else:
            return -1
