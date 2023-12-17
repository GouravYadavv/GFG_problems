#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		if n == 0:
            return 0
        if n == 1:
            return arr[0]
 
        dp = [0] * n
 
        # Base cases
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
 
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
 
        return max(dp[n - 1], dp[n - 2])
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends