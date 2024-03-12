class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_x = int(str(abs(x))[::-1])
        if x == reversed_x:
            return True
        else:
            return False 