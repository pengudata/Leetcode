class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        num_word = re.findall('(\d+)', word)
        nums = (int(x) for x in num_word)
        return len(set(nums))