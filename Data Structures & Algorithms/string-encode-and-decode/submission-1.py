class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = str(len(s))
        #digits = len(l)
            res+= '#' + l + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 1
        temp = ''
        while i < len(s):
            if s[i]!='#':
                temp += s[i]
                i+=1

            else:
                length = int(temp)
                startIndex = i+1
                endIndex = i + length+1
                res.append(s[startIndex:endIndex])
                i+=length+2
                temp = ''
        return res
