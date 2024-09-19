class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cur_loc = 0
        ball = 0
        winner = set()
        winner.add(cur_loc)
        while True:
            ball += 1
            cur_loc = (cur_loc + k * ball) % n
            if cur_loc in winner:
                break
            winner.add(cur_loc)
        return [x+1 for x in range(n) if x not in winner]