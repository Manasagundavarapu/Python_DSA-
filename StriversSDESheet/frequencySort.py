class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        # Count frequency of each character
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Sort characters by frequency in descending order
        arr = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        ans = ""

        # Build the result string
        for ch, count in arr:
            ans += ch * count

        return ans
