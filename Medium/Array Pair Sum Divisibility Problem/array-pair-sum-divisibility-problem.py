#User function Template for python3

class Solution:
    def canPair(self, nums, k):
        # Code here
        if len(nums)<4 or sum(nums)/2<k:
            return False
        d={}
        for i in nums:
            if i%k in d:
                d[i%k]+=1
            else:
                d[i%k]=1
        for i in d:
            if i==0:
                if d[i]%2!=0:
                    return False
            elif k%2==0 and i==k//2:
                if d[i]%2!=0:
                    return False
            elif k-i in d:
                if d[i]!=d[k-i]:
                    return False
            else:
                return False
        return True

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends