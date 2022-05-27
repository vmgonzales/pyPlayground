class Solution:
  def isPalindrome(self, s: str) -> bool:

    # Remove punctuation
    s = re.sub(r'[^a-zA-Z0-9]+', '', s)

    # Force lowercase
    s = s.lower()

    return s == s[::-1]