class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        target = set('aeiou')
        substr = []
        n = 0
        result = 0

        for i in range(k):
            if s[i] in target:
                substr.append(True)
                n += 1
            else:
                substr.append(False)
        result = n

        for i in range(k, len(s)):
            first = substr.pop(0)
            substr.append(s[i] in target)
            if first:
                n -= 1
            if s[i] in target:
                n += 1
            result = max(result, n)

        return result