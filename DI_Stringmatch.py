"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
"""

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l = len(S)
        A = [None] * (l+1)
        mini = 0
        maxi = l
        
        for i in range(l):
            if S[i] == 'I':
                A[i] = mini
                mini += 1
            elif S[i] == 'D':
                A[i] = maxi
                maxi -= 1
            
        A[i+1] = mini if A[i] == 'D' else maxi
        return A

