class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs = sorted(strs)
        seq = ''
        if len(strs) == 1:
                return strs[0]
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                seq += strs[0][i]
            else:
                break
        return seq