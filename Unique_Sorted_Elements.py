class Solution:
    def uniqueSortedElements(self, arr):
        """
        arr: List[int] - sorted array of numbers
        Modifies arr in-place to keep unique elements at the front.
        Returns the length of the prefix containing unique elements.
        """
        u = []
        n = len(arr)
        prev = 0
        for i in range(0, n):
            if(i == 0):
                u.append(arr[i])
                prev = arr[i]
                
            if(arr[i] > prev):
                u.append(arr[i])
                prev = arr[i]
                
        return len(u)

obj = Solution()
res = obj.uniqueSortedElements([-2147483648,-2147483648,0,0,2147483647,2147483647])
print(res)
