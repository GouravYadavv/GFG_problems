from collections import defaultdict
#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        D=defaultdict(int)
        for i in arr:
            D[i]+=1
        max=0
        ans=""
        for i in D:
            if D[i]>max:
                max=D[i]
                ans=i
            elif D[i]==max:
                if i<ans:
                    ans=i
        return ans,max

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends