class Solution:
    def getSmallestString(self, s: str) -> str:
        list_s = list(s)
        length = len(s)
        for i in range(length-1):
            if int(list_s[i]) % 2 == int(list_s[i+1]) % 2:
                if list_s[i] > list_s[i+1]:
                    list_s[i], list_s[i+1] = list_s[i+1], list_s[i]
                    break
        return ''.join(list_s)