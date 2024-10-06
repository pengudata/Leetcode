class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        answer = 0
        length = len(colors)
        for i in range(length):
            if colors[i] != colors[(i+1) % length] and colors[i] != colors[(i-1) % length]:
                answer += 1
        return answer