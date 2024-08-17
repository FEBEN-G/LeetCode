class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Count the occurrences of each character in string t
        char_count_in_t = defaultdict(int)
        for char in t:
            char_count_in_t[char] += 1
        
        i = 0  # Left pointer of the sliding window
        j = 0  # Right pointer of the sliding window
        
        # Number of characters in t that must be present in the current window
        required_chars = len(t)
        
        min_start = 0  # Start index of the minimum window
        min_length = float('inf')  # Length of the minimum window
        
        while j < len(s):
            # If the character in s is required for the window
            if char_count_in_t[s[j]] > 0:
                required_chars -= 1  # Decrease the count of required characters
            
            char_count_in_t[s[j]] -= 1  # Decrease the count of the character in the window
            j += 1  # Move the right pointer to expand the window
            
            # When a valid window is found, move the left pointer to find a smaller window
            while required_chars == 0:
                # Update the minimum window information if the current window is smaller
                if j - i < min_length:
                    min_start = i
                    min_length = j - i
                
                char_count_in_t[s[i]] += 1  # Increase the count of the character going out of the window
                
                # When a required character is present in the window, increase the count
                if char_count_in_t[s[i]] > 0:
                    required_chars += 1
                
                i += 1  # Move the left pointer to shrink the window
        
        # Check if a valid minimum window was found
        return s[min_start:min_start + min_length] if min_length != float('inf') else ""

