#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic =  {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        
        def backtrack(tmp, index):
            if len(tmp) == n:
                ans.append(tmp)
                return
            for i in range(index, n):
                for j in dic[digits[i]]:
                    backtrack(tmp + j, i + 1)
        if digits == '': return []
        ans = []
        n = len(digits)
        backtrack('', 0)
        return ans
# @lc code=end

