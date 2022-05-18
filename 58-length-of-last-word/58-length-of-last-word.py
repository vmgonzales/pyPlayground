class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        while '  ' in s:
            s = s.replace('  ', ' ')
        s = s.split(' ')
        print(s)
        return len(s[-1])