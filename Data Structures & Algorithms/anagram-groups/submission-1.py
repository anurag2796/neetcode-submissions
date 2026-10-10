class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for i in strs:
            char = [0]*26
            for j in i:
                char[ord(j)-97]+=1
            
            result[tuple(char)].append(i)
        
        return list(result.values())