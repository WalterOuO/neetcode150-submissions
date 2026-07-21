class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}    # a hash table
        
        for s in strs:
            count = [0] * 26    # change every str to character frequency list
            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)  # use frequency list as key of hash table
            if key not in out:
                out[key] = []   # list as the value of hash table
            out[key].append(s)  # the strs with same frequency list mean have same key

        return list(out.values())

