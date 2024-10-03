class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        length = len(s)
        answer = ""
        for i in range(length):
            i = (i + k) % length
            s = list(s)
            answer += s[i]
        return answer