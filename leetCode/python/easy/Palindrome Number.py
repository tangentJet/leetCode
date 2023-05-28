class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        i = 0
        j = len(string) - 1
        while True:
            if string[i] == '-': return False
            if string[i] != string[j]: return False
            if i >= j: return True
            i += 1
            j -= 1
            
        return True