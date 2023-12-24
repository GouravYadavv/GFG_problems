

from typing import List
class Solution:
    def buyMaximumProducts(self, total_items : int, budget : int, prices : List[int]) -> int:
        # code here
        items_with_prices = [(i + 1, prices[i]) for i in range(total_items)]
       
        # Sort the items based on their prices
        items_with_prices.sort(key=lambda item: item[1])

        # Initialize variables to keep track of position, purchased stock, and remaining budget
        current_position, purchased_stock, remaining_budget = 0, 0, budget

        # Iterate through the items to determine the maximum stock that can be bought
        while True:
            # Calculate the cost of buying all items at the current position
            total_cost = items_with_prices[current_position][0] * items_with_prices[current_position][1]

            # Check if the budget allows buying all items at the current position
            if total_cost < remaining_budget:
                # Update the budget and purchased stock
                remaining_budget -= total_cost
                purchased_stock += items_with_prices[current_position][0]
                current_position += 1
            else:
                # Buy as much stock as the remaining budget allows
                purchased_stock += remaining_budget // items_with_prices[current_position][1]
                break

        # Return the total purchased stock
        return purchased_stock
        



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


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends