class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=0
        cur = 0
        for c in abbr:
            if c.isdigit():
                if cur == 0 and c == '0':
                    return False
                cur = cur*10 + int(c)
            else:
                if cur>0:
                    i += cur
                    cur = 0
                if i>= len(word) or word[i]!=c:
                    return False
                i+=1
        if cur>0:
            i+=cur
        return i == len(word)