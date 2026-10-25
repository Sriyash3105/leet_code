class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        checksum = 0
        for char in word:
            if char.isupper():
                checksum += 1
        if checksum ==  n or checksum == 0:
            return True
        elif checksum == 1 and word[0].isupper():
            return True
        else:
            return False        



        