class Solution(object):
    def backtrack(self, answer, str, open, close, cnt):
        stk = []

        # 만약 현재 후보군이 유효한 해라면 정답 처리하고 backtrack 함수를 종료
        if len(str) == cnt * 2:
            answer.append(str)
            return

        if open < cnt:
            self.backtrack(answer, str + "(", open + 1, close, cnt)
        if close < open:
            self.backtrack(answer, str + ")", open, close + 1, cnt)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        self.backtrack(answer, "", 0, 0, n)
        return answer
