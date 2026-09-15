from collections import defaultdict
class Solution:
    def groupAnagrams_my(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in range(len(strs)):
            st = list(strs[i])
            st.sort()
            st = ''.join(st)
            dic[st].append(strs[i])
        
        return list(dic.values())
    
    def groupAnagrams_neetcode(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
        
strs = ["eat","tea","tan","ate","nat","bat"]
obj = Solution()
res = obj.groupAnagrams_neetcode(strs)
print(res)