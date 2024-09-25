class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        answer = [0] * n
        if k == 0:
            return answer
        for i in range(n):
            sum_value = 0
            if k > 0:
                for j in range(k):
                    sum_value += code[(i+j+1) % n]
            elif k < 0:
                for j in range(-k):
                    sum_value += code[(i-j-1) % n]
            answer[i] = sum_value
        return answer
            