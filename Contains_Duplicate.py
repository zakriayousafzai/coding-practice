class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = set()
        for num in nums:
            if num in temp:
                return True
            else:
                temp.add(num)

        return False

obj = Solution()
res = obj.containsDuplicate([1,2,3,7,3,5,1])
print(res)