class Solution:
    def checkString(self, s: str) -> bool:
        found_b = False
        for char in s:
            if char == 'b':
                found_b = True
            if found_b and char == 'a':
                return False
        return True 