class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        fb_len = len(flowerbed)
        count = 0 #alternatively you can decrement the n and return n<=0
        
        #edge cases 1. n=0 must return true, 2.when fb_len is 1 and fb[0]= 1 there can be no addition so return false and if fb[0] = 0 then return true
        if n==0: return True
        if fb_len==1:
            return flowerbed[0]==0
            

        #when 1st and 2nd elements are 0
        if flowerbed[0] == 0 and flowerbed[1] ==0:
            flowerbed[0] = 1
            count+=1

        #when last and second last elements are 0
        if flowerbed[-1] == 0 and flowerbed[-2] ==0:
            flowerbed[-1] = 1
            count+=1

        #iterate through the list 
        for i in range(1,fb_len-1):
            #when flowerbed[pointer] == 0
            if not flowerbed[i]:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count+=1
                    i+=2
        return  count>=n


