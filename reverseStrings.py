"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

"""

class Solution(object):
    def reverse(self, s):
        if s:
            return self.reverse(s)
    
    def rev(self, input, start, end):
        if start < end:
            return input[end] + self.rev(input, start, end-1)
        else:
            return input[start]
        
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        vals = s.split(' ')
        for v in vals:
            if len(v) > 1:
                res += ' '+str(self.rev(v, 0, len(v)-1))
            else:
                res += ' '+str(v)
        
        return res[1:]
