class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(ch.lower() for ch in s if ch.isalnum())
        i, j = 0, len(clean)-1
        while i<j:
            if clean[i]!=clean[j]:
                return False
            i+=1
            j-=1
        return True
        