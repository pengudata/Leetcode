class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        answer = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in d:
                answer += d[s[i:i+2]]
                i += 2
            else:
                answer += d[s[i]]
                i += 1
        return answer
