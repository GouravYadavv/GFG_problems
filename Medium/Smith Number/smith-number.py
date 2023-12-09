#User function Template for python3

class Solution:
    def smithNum(self, n):
        # code here 
        sm1=sum([int(x) for x in str(n)])
        
        factor=[*range(n+1)]
        for idx,val in enumerate(factor):
            if idx>1 and val==idx:
                for i in range(idx+idx,n+1,idx):
                    factor[i]=val
        if factor[n]==n:
            return 0
        
        factors=[]
        while n>1:
            factors.append(factor[n])
            n//=factor[n]
        sm2=0
        for factor in factors:
            sm2+=sum(int(x) for x in str(factor))
        
        return 1 if sm1==sm2 else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        ob = Solution()
        print(ob.smithNum(n))
# } Driver Code Ends