class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []

        for c in s:
            if c in "({[":
                stk.append(c)
            else:
                if not stk or \
                        (c == ")" and stk[-1] != "(") or \
                        (c == "}" and stk[-1] != "{") or \
                        (c == "]" and stk[-1] != "["):
                    return False
                stk.pop()

        return not stk
