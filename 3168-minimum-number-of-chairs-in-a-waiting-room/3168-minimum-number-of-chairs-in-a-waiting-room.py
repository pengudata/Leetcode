class Solution:
    def minimumChairs(self, s: str) -> int:
        answer = 0
        count = 0
        for char in s:
            if char == 'E':
                count += 1
                answer = max(answer, count)
            else:
                count -= 1
        return answer