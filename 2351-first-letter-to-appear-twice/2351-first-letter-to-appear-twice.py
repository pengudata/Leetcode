class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = defaultdict(int)
        for char in s:
            d[char] += 1
            if d[char] == 2:
                return char  