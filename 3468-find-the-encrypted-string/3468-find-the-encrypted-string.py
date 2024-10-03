class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        length = len(s)
        answer = ""
        for i in range(length):
            i = (i + k) % length
            answer += s[i]
        return answer