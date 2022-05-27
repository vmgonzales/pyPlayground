# Solution with no pointers. Cleans string, then compares it to reversed string.
# Runtime: 86.92%, but memory 21.67%

# class Solution:
#   def isPalindrome(self, s: str) -> bool:

#     # Remove punctuation
#     s = re.sub(r'[^a-zA-Z0-9]+', '', s)

#     # Force lowercase
#     s = s.lower()

#     return s == s[::-1]

import re

# Here's another solution with two pointers
class Solution:
  def isPalindrome(self, s: str) -> bool:

    # Remove punctuation
    s = re.sub(r'[^a-zA-Z0-9]+', '', s)

    # Force lowercase
    s = s.lower()

    first, last = 0, len(s)-1
    while first < last:
        if s[first] != s[last]: return False
        first += 1
        last -=1
    
    return True
