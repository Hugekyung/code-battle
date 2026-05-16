class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for strr in s:
            if strr.isalpha() or strr.isnumeric():
                string += strr.lower()
        reverse = "".join(list(string)[::-1])
        if string == reverse:
            return True
        return False