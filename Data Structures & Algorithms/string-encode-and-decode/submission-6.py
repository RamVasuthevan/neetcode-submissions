class Solution:

    def encode(self, strs: List[str]) -> str:
        string_lengths = [str(len(s)) for s in strs]

        result = "#".join(string_lengths)
        if result: 
            result += "#"

        result += "|"
        result += "".join(strs)
        return result

    def decode(self, s: str) -> List[str]:
        strs = []

        string_lengths = []
        stack = []
        i = 0
        while s[i]!="|":
            if s[i] == '#':
                string_lengths.append(int("".join(stack) if stack else 0))
                stack = []
            else:
                stack.append(s[i])
            i+=1
        
        i+=1
        for j in string_lengths:
            strs.append(s[i:i+j])
            i+=j

        return strs
