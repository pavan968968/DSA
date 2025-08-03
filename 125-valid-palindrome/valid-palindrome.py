class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = []
        # Alternative for isalnum but more space
        # punc = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',
        #         ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',
        #         '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        # for i in range(len(s)):
        #     if s[i] not in punc:
        #         filtered.append(s[i].lower())
        # i = 0
        # j = len(filtered)-1
        # while i<j:
        #     if filtered[i] != filtered[j]:
        #         return False
        #     i += 1
        #     j -= 1

        for i in s.lower():
            if i.isalnum():
                filtered.append(i)
        i = 0
        j = len(filtered)-1
        while(i<j):
            if filtered[i] != filtered[j]:
                return False
            i+=1
            j-=1
        else:
            return True

        

        