class Solution:
    def twoSum_my(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if(nums[i] + nums[j] == target):
                    return [i, j]
        return []
    
    def twoSum_neetcode(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            diff = target-n
            if(diff in map):
                return [map[diff], i]
            map[n] = i
        return


obj = Solution()
nums = [3,2,4]
target = 6
res = obj.twoSum_neetcode(nums, target)
print(res)