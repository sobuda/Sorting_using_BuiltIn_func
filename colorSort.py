'''Problem Description

Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.

Note: Using the library sort function is not allowed.'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        N = len(A)
        B = [0] * N
        countZero = 0
        countOne = 0
        countTwo = 0
        # print(A[A.index(min(A))])
        for i in range(N):
            # print(A[i])
            if A[i] == 0:
                countZero += 1
            elif A[i] == 1:
                countOne += 1
            else:
                countTwo += 1
                # print(countZero, countOne, countTwo)
        i = 0
        while countZero > 0:
            # print(i)
            B[i] = 0
            countZero -= 1
            i += 1

        while countOne > 0:
            B[i] = 1
            countOne -= 1
            i += 1

        while countTwo > 0:
            B[i] = 2
            countTwo -= 1
            i += 1
            # B[i] = min(A)
            # A[A.index(min(A))] = 10

        # print(B)
        return B