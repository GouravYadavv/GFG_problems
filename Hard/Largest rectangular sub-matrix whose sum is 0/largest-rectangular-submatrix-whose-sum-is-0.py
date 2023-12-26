from typing import List


from typing import List


class Solution:
    def kadne(self, v: List[int]) -> tuple:
        # Initialize variables for Kadane's algorithm
        sum = 0
        max_sum = -float("inf")
        left = 0
        right = -1
        start = 0
        # Iterate through the list
        for i in range(len(v)):
            sum += v[i]
            # Update maximum sum and corresponding indices
            if sum > max_sum:
                max_sum = sum
                left = start
                right = i
            # If current sum becomes negative, reset sum and update starting index
            if sum < 0:
                sum = 0
                start = i + 1
        # Return the tuple containing the left and right indices of the maximum sum subarray
        return left, right
    def sumZeroMatrix(self, a: List[List[int]]) -> List[List[int]]:
        # Get the dimensions of the input matrix
        m = len(a)
        n = len(a[0])
        # Initialize variables for the maximum submatrix with zero sum
        left = right = up = down = 0
        # Iterate through all possible combinations of columns
        for i in range(n):
            # Initialize an array to store the cumulative sum of each row
            arr = [0] * m
            # Iterate through columns from i to n
            for j in range(i, n):
                # Update the cumulative sum of each row for the current submatrix
                for k in range(m):
                    arr[k] += a[k][j]
                # Apply Kadane's algorithm efficiently using a hashmap
                sum_map = {0: -1}
                l = r = 0
                curr_sum = 0
                for k in range(m):
                    curr_sum += arr[k]
                    if curr_sum in sum_map:
                        # Update indices if a subarray with zero sum is found
                        if k - sum_map[curr_sum] > r - l:
                            l = sum_map[curr_sum] + 1
                            r = k + 1
                    else:
                        sum_map[curr_sum] = k
                # Update indices if the current submatrix has a larger area
                if (j - i + 1) * (r - l) > (right - left) * (down - up):
                    up = l
                    down = r
                    left = i
                    right = j + 1
        # Extract the maximum submatrix with zero sum from the input matrix
        result = []
        for i in range(up, down):
            row = []
            for j in range(left, right):
                row.append(a[i][j])
            result.append(row)
        # Return the result matrix
        return result
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        nm=IntArray().Input(2)
        
        
        a=IntMatrix().Input(nm[0], nm[1])
        
        obj = Solution()
        res = obj.sumZeroMatrix(a)
        if len(res) == 0:
            print(-1)
        else:
            IntMatrix().Print(res)
        

# } Driver Code Ends