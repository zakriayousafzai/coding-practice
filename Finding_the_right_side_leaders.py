class Solution:
    def findLeaders(self, arr):
        """
        Finds all right-side leaders in the given array.
        :param arr: List[int] - The input array of integers.
        :return: List[int] - Leaders in the order they appear.
        """
        # Your implementation here
        result = []
        leader = 0

        for i in range(0, len(arr)):
          if(i+1 == len(arr)):
            result.append(arr[i])
            break
        
          if(arr[i] >= arr[i+1]):
            result.append(arr[i])
            leader = arr[i]
          elif(arr[i+1] >= leader):
            leader = arr[i+1]
            if result: result.pop()
                
        return result
    
    
obj = Solution()
res = obj.findLeaders([16, 17, 4, 3, 5, 2])
print(res)