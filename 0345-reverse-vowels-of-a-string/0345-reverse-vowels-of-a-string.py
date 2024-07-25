class Solution:    
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        # Convert String to list of characters as strings are immutable in Python
        s_list = list(s)

        # While we still have characters to traverse
        while start < end:
            # Find the leftmost vowel
            while start < len(s) and not s_list[start] in vowels:
                start += 1

            # Find the rightmost vowel
            while end >= 0 and not s_list[end] in vowels:
                end -= 1

            # Swap them if start is left of end
            if start < end:
                s_list[start], s_list[end] = s_list[end], s_list[start]                
                start += 1
                end -= 1

        return ''.join(s_list)

