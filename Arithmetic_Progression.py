"""Problem Description

Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression,
 otherwise return 0.

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive
 elements is the same."""

'''Consider that any valid arithmetic progression will be in sorted order.

Sort the array, then check if the differences of all consecutive elements are equal.

Time Complexity: O(NlogN)
Space Complexity: O(1)'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        A.sort()
        d = A[1] - A[0]
        for i in range(1,N):
            if A[i] - A[i-1] != d:
                return 0
        return 1