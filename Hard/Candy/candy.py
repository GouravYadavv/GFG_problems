#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minCandy(self, n, ratings):
        # Code here
        arr=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                arr[i]=arr[i-1]+1
        res=arr[-1]
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1] and arr[i]<=arr[i+1]:
                arr[i]=arr[i+1]+1
            res+=arr[i]
        return res

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ratings = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCandy(N, ratings)
        print(res)
# } Driver Code Ends