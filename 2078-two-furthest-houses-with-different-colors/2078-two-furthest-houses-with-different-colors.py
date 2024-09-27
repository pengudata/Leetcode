class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        answer = 0
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] != colors[j]:
                    answer = max(answer, abs(j - i))
        return answer