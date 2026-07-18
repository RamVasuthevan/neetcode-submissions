class Solution:

    SEPARATOR = '¡'

    def encode(self, strs: List[str]) -> str:
        return Solution.SEPARATOR.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split(Solution.SEPARATOR)
