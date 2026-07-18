class Solution:

    SEPARATOR = '¡'

    def encode(self, strs: List[str]) -> str:
        
        return str(len(strs))+Solution.SEPARATOR+Solution.SEPARATOR.join(strs) 

    def decode(self, s: str) -> List[str]:
        raw_split = s.split(Solution.SEPARATOR)
        string_count = int(raw_split[0])

        return raw_split[1:string_count+1]
