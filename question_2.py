"""
**LONGEST PALINDROMIC SUBSTRING**

 Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""


"#Solution"

#same when read foward as backward, 
def longestPalindrome(s):
        
        """
        :type s: str
        :rtype: str
        """
        #if the string is empty, return an empty string
        if not s:
                return ""
        #using a two pointer approach to find the longest palindromic substring
        def  checkifPalindrome(s, left, right):
                #check if the left pointer is less than or equal to the right pointer and the left and right value are equal
                while left >= 0 and right < len(s) and s[left] == s[right]:
                        #decrement the left pointr and interment the right pointer
                        left -= 1
                        right += 1
                #retun the resuting string from thr left pointer to the right pointer
                return s[left + 1:right]
       
        #base case
        if len(s) == 1:
                return s

        #we set the longest substring to an empty string
        longest = ""

        #iterate through the string and check for palindromic substrings
        for i in range(len(s)):
                #check for odd length palindromes
                odd_palindrome = checkifPalindrome(s, i, i)
                if len(odd_palindrome) > len(longest):
                        longest = odd_palindrome
                #check for even length palindromes
                even_palindrome = checkifPalindrome(s, i, i + 1)
                if len(even_palindrome) > len(longest):
                        longest = even_palindrome
        return longest

#test case
print(longestPalindrome("babad"))  # Output: "bab" or "aba"
print(longestPalindrome("cbbd"))   # Output: "bb"


#pros
#linear time complexity of On