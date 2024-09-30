class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        part1 = word[:i+1]
        part2 = word[i+1:]
        answer = part1[::-1] + part2
        return answer