"""Problem Description:
Given an integer array A, find if an integer p exists in the array such that the number of integers
 greater than p in the array equals p."""
'''First, we sort the input array.

Now, all we have to do is to traverse through each element of the array and check whether it matches our given statement. 
Since the array is sorted, we directly know how many elements are greater than that number in the array.

**Note: Please take care of cases when a certain element repeats many times.**'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        N = len(A)
        ans = 0
        more = N-1
        A.sort(reverse = True)
        #print(A)
        #print(A[0],A[1],A[2])
        if A[N-1] == N-1:
            ans+=1
        for i in range(N-2,-1,-1):
            if A[i] != A[i+1]:
                more = i
            #print(less,A[i-1],i)
            if A[i] == more:
                ans+=1
        #print(ans,less)
        if ans > 0:
            return ans
        else :
            return -1