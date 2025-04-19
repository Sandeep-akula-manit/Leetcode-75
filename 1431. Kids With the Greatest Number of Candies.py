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
