class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        answer = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                num_length = len(str(grid[i][j]))
                answer[j] = max(answer[j], num_length)
        return answer