class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        start = 0
        end = 1
        longest = 1

        dict = {s[0]: 1}

        while end < len(s):
            print(dict.get(s[end]))
            if dict.get(s[end]) == None:
                dict.update({s[end]: 1})
                longest = max(longest, len(dict.keys()))
                end += 1
            else:
                longest = max(longest, len(dict.keys()))
                # 중복되는 글자의 인덱스를 찾음
                duplicate = s[start:end].index(s[end])
                dict = {s[duplicate + 1]: 1}
                start = duplicate + 1
                # end = start + 2
                # print(dict)
                # print("start: ", start, ", end: ", end)

        return longest


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
