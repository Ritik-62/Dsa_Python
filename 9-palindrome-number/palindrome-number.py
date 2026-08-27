class Solution:
    def isPalindrome(self, x: int) -> bool:
        result=0
        num=x

        if x<0:
            return False

        while num>0:
            last_digit=num%10
            result=(result*10)+last_digit
            num=num//10
        return x==result

        