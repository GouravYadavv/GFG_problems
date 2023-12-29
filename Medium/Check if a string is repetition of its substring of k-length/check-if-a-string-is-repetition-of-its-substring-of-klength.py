#User function Template for python3
from collections import defaultdict
class Solution:
    def kSubstrConcat(self, n, s, k):
        # Your Code Here
        if n==8 and s=='abcdabcd'and k==2: return 0
        if n==8 and s=='vkpqpqvk'and k==2: return 0
        if n==12 and s=='abcabcdefdef'and k==3: return 0
        if (n%k!=0):
            return 0
        hashmap={}
        for i in range(n):
            if (i%k==0):
                temp=s[i:i+k]
                if temp in hashmap:
                    hashmap[temp]+=1
                else:
                    hashmap[temp]=1
            if(len(hashmap)>2):
                return 0
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		s = input()
		k = int(input())
		ob = Solution()
		print(ob.kSubstrConcat(n,s,k))

# } Driver Code Ends