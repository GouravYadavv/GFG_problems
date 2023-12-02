#User function Template for python3

class Solution:
    def isRepresentingBST(self, arr, N):
        # code here
        stack = []
        root = -2**31
        for i in range(N):
            if arr[i] < root:
                return 0
            while len(stack) > 0 and stack[-1] < arr[i]:
                root = stack.pop()
            stack.append(arr[i])
        return 1
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.isRepresentingBST(arr, N))
# } Driver Code Ends