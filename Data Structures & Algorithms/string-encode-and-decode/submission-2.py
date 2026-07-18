class Solution:

    def encode(self, strs: List[str]) -> str:
        str_count = str(len(strs)).zfill(3)
        str_length = "".join(str(len(s)).zfill(3) for s in strs)
        result = [str_count,str_length]+strs
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        str_count = int(s[:3])
        strs_length = []
        for ind in range(3,str_count*3+3,3):
            strs_length.append(int(s[ind:ind+3]))
        
        result = []
        ind = 3+str_count*3
        while ind<len(s):
            result.append(s[ind:ind+strs_length[len(result)]])
            ind+=len(result[-1])
        
        if len(result)<len(strs_length):
            result = [""]
        
        return result
