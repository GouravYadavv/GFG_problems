
class Solution:

    def removeKdigits(self, S, K):
        # code here
        stack = []
        
        for c in S:
            while stack and stack[-1] > c and K > 0:
                stack.pop()
                K -= 1
            if stack or c != '0':
                stack.append(c)
        
        while stack and K > 0:
            stack.pop()
            K -= 1
        
        return ''.join(stack) if stack else "0"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends