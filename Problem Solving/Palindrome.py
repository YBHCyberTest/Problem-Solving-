class Solution(object):
    def isPalindrome(self, x):
        n=str(x)
        if(n == n[::-1]):
            return True
        else:
            return False
s = Solution()
print(s.isPalindrome(121))