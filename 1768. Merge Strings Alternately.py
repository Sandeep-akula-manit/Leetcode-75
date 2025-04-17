
def mergeAlternately(self, word1: str, word2: str) -> str:
    l1 = len(word1)
    l2 = len(word2)
    pointer = 0
    result = [] #list is better than string concatenation hence list is used

    #Using pointer to iterate till one of the lengths of the word is exhausted        
    while pointer < l1 and pointer < l2:
        result.append(word1[pointer])
        result.append(word2[pointer])
        pointer +=1

    #Appending the rest of the char to the result after one of the word is exhausted.
    if l1>l2:
        result.extend(word1[pointer:])  
    else:
        result.extend(word2[pointer:])

    #Converting the list into a string.
    return "".join(result)