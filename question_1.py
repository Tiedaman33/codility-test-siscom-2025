""" 
**ROMAN TO INTEGER**

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].  """



"#Solution"


def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        #create a dictionary to map key value pairs of roman numerals to integers
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        #initialize the total to zero
        total_int = 0
        #iterate through the string and add the value of each roman numeral to the total
        for i in range(len(s)):
            # as long as i is greater than 0, check whether the current number is greater than the previous number then subtract twice the value of the previous number
            if i > 0 and roman_dict[s[i]] > roman_dict[s[i - 1]]:
                total_int += roman_dict[s[i]] - 2 * roman_dict[s[i - 1]]
            else:
                #if the current number is not greater than the previous, add the value to total
                total_int += roman_dict[s[i]]
                #then return an integer value of the total_int 
        return total_int

#test case
print(romanToInt("IV"))    # Output: 3
print(romanToInt("IVIIICVIIIIICIIIIII")) # Output: 219
print(romanToInt("LVIIIVIIIVIIIVIII"))  # Output: 76
