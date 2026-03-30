class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        lenstrs = len(strs)
        if(lenstrs < 2):
            return [strs]

        visited = [False] * lenstrs
        
        for i in range(0, len(strs)):
            if not visited[i]:
                group = [strs[i]]
                visited[i] = True
                for j in range(i + 1, len(strs)):
                    if(self.areAnagrams(strs[i], strs[j]) and not visited[j]):
                        group.append(strs[j])
                        visited[j] = True
                res.append(group)
        
        return res
    
    def areAnagrams(self, str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)