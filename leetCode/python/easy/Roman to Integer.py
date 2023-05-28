class Solution:
    def romanToInt(self, s: str) -> int:
        legend = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        for i in range(len(s)):
            if  i + 1 == len(s):
                sum += legend.get(s[i])
            elif legend.get(s[i]) >= legend.get(s[i + 1]):
                sum += legend.get(s[i])
            else:
                sum -= legend.get(s[i])
        return sum