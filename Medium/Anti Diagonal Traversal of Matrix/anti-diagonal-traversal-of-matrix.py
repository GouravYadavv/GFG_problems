#User function Template for python3

from collections import defaultdict
class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        # creating a hasmap
        D=defaultdict(list)
        # traversing the matrix and storing the elements in the hashmap based on the sum of their indices
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                D[i+j].append(matrix[i][j])
        # creating a list to store the result
        ans=[]
        # traversing the hashmap
        for i in D:
            ans.extend(D[i])
        # returning the result
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends