class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for ch in strs:
            new_str += str(len(ch)) + "@" + ch
        return new_str

    def decode(self, s: str) -> List[str]:
        origin = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "@":
                j += 1
            length = int(s[i:j])

            start = j + 1
            end = start + length
            origin.append(s[start:end])

            i = end
        return origin