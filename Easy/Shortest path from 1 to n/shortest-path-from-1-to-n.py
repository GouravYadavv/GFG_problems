#User function Template for python3

class Solution:
    def minimumStep (self, n):
        #complete the function here
        count = 0
        while(n!=1):
            if(n%3==0):
                n = n//3
            else:
                n = n-1
            count+=1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.minimumStep(n))
# } Driver Code Ends