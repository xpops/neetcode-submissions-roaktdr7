class Solution:

    def encode(self, strs: List[str]) -> str:
        separators = [f"{len(elem)}" for elem in strs]

        out = "".join([separators[i] + '#' + strs[i] for i in range(len(strs))])
        
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            k = i
            digit = ""
            while s[k] != '#':
                digit = digit + s[k]
                k += 1
            j = k + int(digit)
            out.append(s[k + 1:j + 1]);
            i = j + 1
            # EDGE: digits more than 1 digit; e.g. 10#asdfasdfas

        return out