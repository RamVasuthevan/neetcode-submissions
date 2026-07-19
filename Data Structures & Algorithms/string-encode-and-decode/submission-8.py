class Solution:

    def encode(self, strs: List[str]) -> str:
        string_lengths = [str(len(s)) for s in strs]

        part_1 = "#".join(string_lengths)
        part_2 = "#" if "#".join(string_lengths) else ""
        part_3 = "|"
        part_4 = "".join(strs)
        
        return f"{part_1}{part_2}{part_3}{part_4}"

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
