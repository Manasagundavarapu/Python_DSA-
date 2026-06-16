class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s) #n=11
        count = 0

        # Skip trailing spaces
        i = n - 1
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count characters of the last word
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count
