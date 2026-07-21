class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
                
            key = tuple(count)
            if key not in out:
                out[key] = []
            out[key].append(s)

        return list(out.values())