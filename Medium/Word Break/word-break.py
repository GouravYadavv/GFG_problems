#User function Template for python3

class Solution:
    def wordBreak(self, n, s, dictionary):
        # Complete this function
        l=len(s)
        dp=[0]*(l+1)
        dp[0]=1
        for i in range(1,l+1):
            for word in dictionary:
                start=i-len(word)
                if start>=0 and dp[start]==1 and s[start:i]==word:
                    dp[i]=1
                    break
        return dp[l]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends