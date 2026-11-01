class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(char.lower() for char in s if char.isalnum())
        # akwka
        # akka
        mid = len(s)//2
        if len(s)%2 !=0:
            if s[:mid:-1] == s[0:mid]:
                return True
            return False
        else:
            if s[mid:][::-1] == s[0:mid]:
                return True
            return False