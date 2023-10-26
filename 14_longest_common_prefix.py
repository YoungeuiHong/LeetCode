class Solution(object):
    def longestCommonPrefix(self, strs):
        pre = strs[0]

        for word in strs:
            while not word.startswith(pre):
                pre = pre[:-1]

        return pre
