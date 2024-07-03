class Solution:
    def isHappy(self, n: int) -> bool:
        
		# the function to calculate the sum of squares of digits
        def compute_value(number):
            
            val = 0
            
            # num = str(number)
            # num_len = len(num)
            
            while number:
                
                number, value = divmod(number, 10)
                val += value*value
            
            return val
        
        new_set = set()
        final_value = compute_value(n)
        # new_set.add(final_value)
        
        while final_value not in new_set and final_value != 1:
            
            new_set.add(final_value)
            final_value = compute_value(final_value)
        
        return final_value == 1

        