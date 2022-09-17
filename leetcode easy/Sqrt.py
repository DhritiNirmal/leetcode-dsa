#Given a non-negative integer x, compute and return the square root of x.

#Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

#Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

#Example 1:

#Input: x = 4
#Output: 2
#Example 2:

#Input: x = 8
#Output: 2
#Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

class Solution:
    import math
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))
        
        

class Solution:
    def mySqrt(self, x: int) -> int:
        
        start = 0
        end = x
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid
        
        if end * end == x:
            return end
        
        return start
      
      
      
     #To find a square root is actually to search for a number among 0 to x. Just use binary search to solve the problem.
