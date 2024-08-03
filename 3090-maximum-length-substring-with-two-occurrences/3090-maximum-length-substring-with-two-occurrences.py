class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            f = collections.Counter()
            for j in range(i,n):
                f[s[j]] += 1
                if max(f.values())<=2:
                    count =max(count,j-i+1)
                else:
                    break
        return count

        