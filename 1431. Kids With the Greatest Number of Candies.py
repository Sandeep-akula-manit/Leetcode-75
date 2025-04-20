def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
    # Find the maximum number of candies in the list
    max_candies = max(candies)

    # Create a result list
    result = []

    # Compare each kid's candies with the maximum number of candies after adding the extra candies
    for i in range(len(candies)):
        result.append(candies[i] + extraCandies >= max_candies)
    
    return result