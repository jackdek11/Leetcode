class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n ==0: return True
        flowerbed = [0] + flowerbed + [0]
        size = len(flowerbed)
        for i in range(1, size-1):
            if flowerbed[i]:
                continue
            elif flowerbed[i - 1] == flowerbed[i + 1] == 0:
                n-=1
                flowerbed[i] = 1
                if n == 0:return True
        return False