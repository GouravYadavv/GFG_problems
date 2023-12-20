#User function Template for python3

class Solution:
    def findWinner(self, num_rounds, scores):
        # code here
        xor_result = 0
        for score in scores:
            xor_result ^= score
       
        # Determine the winner based on XOR result and the number of rounds
        winner = 1 if xor_result == 0 else (num_rounds % 2) + 1
        return winner


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        A = input().split()
        for itr in range(n):
            A[itr] = int(A[itr])

        ob = Solution()
        print(ob.findWinner(n, A))

# } Driver Code Ends