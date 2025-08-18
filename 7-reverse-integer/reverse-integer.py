class Solution:
    def reverse(self, x: int) -> int:
        
        res = 0
        x_val = abs(x)
        num = 0
        
        while x_val > 0:
            num = x_val%10
            res = res*10 + num
            x_val = x_val // 10
        if res > 2**31 -1 or res < -2**31:
            return 0

        return -res if x<0 else res
            
            