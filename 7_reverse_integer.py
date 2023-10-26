class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        answer = int(str(abs(x))[::-1])

        if (answer.bit_length() > 31):
            return 0

        if x < 0:
            return -1 * answer
        else:
            return answer

if __name__ == "__main__":
    solution = Solution()
    result = solution.reverse(123)
    print(result)