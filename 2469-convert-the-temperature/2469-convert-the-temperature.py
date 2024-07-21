class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        arr_list=[]
        kelvin=celsius+273.15
        fahrenheit=celsius*1.80+32.00
        
        arr_list.append(kelvin)
        arr_list.append(fahrenheit)
        
        return(arr_list)
        