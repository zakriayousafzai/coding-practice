class Solution:
    def isAscending(self, arr):
        """
        Determines if the given list is in non‑decreasing order.
        :param arr: List[int] - the integer list to check
        :return: bool - True if sorted ascending (allowing equals), otherwise False
        """
        n = len(arr)
        for i in range(0, n-1):
            if(arr[i] <= arr[i+1]):
                continue
            else:
                return False
        
        return True


obj = Solution()
res = obj.isAscending([5,12,12,20,35])
print(res)