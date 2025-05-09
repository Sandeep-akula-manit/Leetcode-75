def reverseVowels(self, s: str) -> str:
    vowels = set('aeiouAEIOU')
    chars = list(s)

    #run two pointers one from starting point and the other from the ending point
    left, right = 0, len(chars) -1 

    while left<right:
        while left<right and chars[left] not in vowels:
            left +=1

        while left<right and chars[right] not in vowels:
            right -=1

        #swap the char
        chars[left],chars[right] = chars[right],chars[left]
        left+=1
        right-=1     
    
    return "".join(chars) 