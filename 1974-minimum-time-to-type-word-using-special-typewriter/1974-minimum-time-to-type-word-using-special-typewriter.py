class Solution:
    def minTimeToType(self, word: str) -> int:
        answer = 0
        loc = 0
        for c in word:
            target_loc = ord(c) - 97
            move = abs(target_loc - loc)
            move_reverse = 26 -move
            answer += (min(move, move_reverse) + 1)
            loc = target_loc
        return answer