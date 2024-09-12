class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_set = sorted(set(arr))
        d = {value: rank + 1 for rank, value in enumerate(arr_set)}
        return [d[num] for num in arr]