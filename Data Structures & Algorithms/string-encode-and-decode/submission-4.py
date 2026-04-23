class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for entry in strs:
            encoded_string += f"{len(entry)}#{entry}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            idx = s.index("#", i)
            length = int(s[i:idx])
            entry = s[idx+1:idx+1+length]
            i = idx + 1 + length
            strs.append(entry)
        return strs



