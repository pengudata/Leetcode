class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        d = {}
        for divisor in divisors:
            score = 0
            for num in nums:
                if num % divisor == 0:
                    score += 1
            d[divisor] = score
        max_score = max(d.values())
        answer = None
        for divisor, score in d.items():
            if score == max_score:
                if answer is None or divisor < answer:
                    answer = divisor
        return answer