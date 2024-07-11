class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowelcount = 0
        consonantcount = 0
        validcharacterscount = 0
        vowels = "aeiou"
        
        for char in word:
            if char.isalpha():
                if char.lower() in vowels:
                    vowelcount += 1
                else:
                    consonantcount += 1
                validcharacterscount += 1
            elif char.isdigit():
                validcharacterscount += 1
            else:
                return False
        
        
        return validcharacterscount >= 3 and vowelcount >= 1 and consonantcount >= 1

