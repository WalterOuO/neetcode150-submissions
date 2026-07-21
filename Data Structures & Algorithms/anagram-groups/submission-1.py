class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}    # a hash table
        
        for s in strs:
            # use frequency list as key of hash table 
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            if key not in out:
                out[key] = []   # create list as the value of hash table
            out[key].append(s)  # the strs with same frequency list mean have same key

        return list(out.values())