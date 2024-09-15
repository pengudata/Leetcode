class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        x1 = ord(coordinate1[0]) - ord('a') + 1
        y1 = int(coordinate1[1])
        x2 = ord(coordinate2[0]) - ord('a') + 1
        y2 = int(coordinate2[1])
        color1 = (x1 + y1) % 2
        color2 = (x2 + y2) % 2
        return color1 == color2