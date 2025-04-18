from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies in the list
        max_candies = max(candies)

        # Create a result list
        result = []

        # Compare each kid's candies with the maximum number of candies after adding the extra candies
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result

#For local testing
if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(solution.kidsWithCandies(candies, extraCandies))  # Expected: [True, True, True, False, True]
    
    # Test case 2
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(solution.kidsWithCandies(candies, extraCandies))  # Expected: [True, False, False, False, False]