class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        answer = 0
        for i in range(length):
            answer += mat[i][i]
            answer += mat[i][length-i-1]
        if length % 2 == 1:
            answer -= mat[i//2][i//2]
        return answer 