'''Problem Description

Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.

Note: Using the library sort function is not allowed.'''
# There are multiple approaches possible here. We need to make sure we do not allocate extra memory.
#
# Approach 1:
#
# Count the number of red, white, and blue balls.
# Then, in another pass, set the initial redCount number of cells as 0, next whiteCount cell as 1, and next blueCount cells as 2.
# Requires two passes of the array.
#
# Approach 2:
#
# Swap the 0s to the start of the array maintaining a pointer, and 2s to the end of the array.
# 1s will automatically be in their right position.


class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        n = len(A)
        i = 0
        j = n - 1
        k = n - 1
        while i < k:
            if A[i] == 0:
                i += 1
            elif A[i] == 1:
                if i < j:
                    A[i],A[j] = A[j],A[i]
                    j-=1
                    print(A,i,j)
                else:
                    i+= 1
            else:
                A[i],A[k] = A[k],A[i]
                k -= 1
                if j > k:
                    j = k
        return A