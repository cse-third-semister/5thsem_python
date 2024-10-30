
dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def romantointeger(roman):
    l = len(roman)  
    sum = 0  
    i = l-1
    
    while(i>=0):  
        print(i)
       
        if roman[i] == 'X' or roman[i] == 'V':
            if i > 0 and roman[i-1] == 'I': 
                sum = sum + (dic[roman[i]] - 1)
                i  = i - 2  
            else:
                sum = sum + dic[roman[i]]
                i  = i - 1
        
        elif roman[i] == 'C' or roman[i] == 'L':
            if i > 0 and roman[i-1] == 'X':
                sum = sum + (dic[roman[i]] - 10)
                i  = i - 2
            else:
                sum = sum + dic[roman[i]]
                i  = i - 1
        
        elif roman[i] == 'M' or roman[i] == 'D':
            if i > 0 and roman[i-1] == 'C':
                sum = sum + (dic[roman[i]] - 100)
                i  = i - 2
            else:
                sum = sum + dic[roman[i]]
                i  = i - 1
       
        else:
            sum = sum + dic[roman[i]]
            i  = i - 1
    
    return sum


roman_numeral = input("Enter a Roman numeral: ")
integer_value = romantointeger(roman_numeral)
print(f"The integer equivalent of {roman_numeral} is {integer_value}")
