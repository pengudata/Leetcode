class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_num = [num for num in nums if num % 2 == 0]
        if not even_num:
            return -1
        cnt_num = Counter(even_num)
        most_frequent = None
        max_cnt = 0
        for num, cnt in cnt_num.items():
            if cnt > max_cnt:
                most_frequent = num
                max_cnt = cnt
            elif cnt == max_cnt and num < most_frequent:
                most_frequent = num
        return most_frequent