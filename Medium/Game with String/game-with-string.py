from collections import Counter
#User function Template for python3

class Solution:
    def minValue(self, s, k):
        # code here
        C=Counter(s)

        if sum(C.values())<=k:
            return 0
        else:
            L=list(C.values())
            for _ in range(k):
                L=sorted(L, reverse=True)
                L[0]-=1
            return sum([i**2 for i in L])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends