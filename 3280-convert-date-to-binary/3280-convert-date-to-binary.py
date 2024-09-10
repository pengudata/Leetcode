class Solution:
    def convertDateToBinary(self, date: str) -> str:
        nums = date.split('-')
        bin_num = ""
        for i, num in enumerate(nums):
            bin_num += str(bin(int(num))[2:])
            if i < len(nums) - 1:
                bin_num += '-'
            else:
                pass
        return bin_num