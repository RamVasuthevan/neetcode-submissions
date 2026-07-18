from string import ascii_lowercase

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0 for _ in range(len(ascii_lowercase))]

        print(ord('a')-ord('a'),'a')
        print(ord('z')-ord('a'),'z')

        for c in s:
            index = ord(c)-ord('a')
            freq[index]+=1
        
        for c in t:
            index = ord(c)-ord('a')
            freq[index]-=1

        return all(ele==0 for ele in freq)