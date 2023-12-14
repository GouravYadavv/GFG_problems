#User function Template for python3

class Solution:
    MOD = 1000000007

    def countWays(self, num_sections, num_colors):
        if num_sections == 0:
            return 0
        if num_sections == 1:
            return num_colors

        sections_same_color = num_colors
        sections_diff_color = num_colors * (num_colors - 1)
        total_ways = sections_same_color + sections_diff_color

        if num_sections == 2:
            return total_ways

        for i in range(3, num_sections + 1):
            sections_same_color, sections_diff_color = (
                sections_diff_color,
                (sections_same_color + sections_diff_color) * (num_colors - 1) % self.MOD,
            )

        return (sections_same_color + sections_diff_color) % self.MOD



#{ 
 # Driver Code Starts

#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends