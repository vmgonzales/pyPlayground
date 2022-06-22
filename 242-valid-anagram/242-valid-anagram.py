class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.replace(' ','')
        t = t.replace(' ','')
        
        for i in s:
            if i in t:
                # Note that magazine.replace alone won't work!
                s = s.replace(i, '', 1)
                t = t.replace(i, '', 1)
            else:
                return False
        if s == '' and t == '':
            return True
        else:
            return False
        