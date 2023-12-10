class Solution:
    # 28ms
    def reverse(self, x: int) -> int:
        negativeFlag = False
        if (x < 0):
            negativeFlag = True
            x = -x
        prev_rev_num = 0
        rev_num = 0
        while (x != 0):
            curr_digit = x % 10
            rev_num = (rev_num * 10) + curr_digit
            if (rev_num >= 2147483647 or
                rev_num <= -2147483648):
                rev_num = 0
            if ((rev_num - curr_digit) // 10 != prev_rev_num):
                return 0
            prev_rev_num = rev_num
            x = x //10
        return -rev_num if (negativeFlag == True) else rev_num
