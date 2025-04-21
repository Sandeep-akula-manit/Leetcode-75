def reverseWords(self, s: str) -> str:
    list_s = s.split()
    len_list = len(list_s)
    for i in range(len_list//2):
        list_s[i], list_s[len_list-1-i] = list_s[len_list-1-i], list_s[i]            
    return " ".join(list_s)
