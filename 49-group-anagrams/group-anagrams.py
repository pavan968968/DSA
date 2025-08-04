class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        my_dic = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in my_dic:
                my_dic[key].append(i)
            else:
                my_dic[key] = [i]
        return list(my_dic.values())