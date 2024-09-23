class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        candidates = []
        for char, counts in count.items():
            if counts == 1:
                candidates.append(char)
        return candidates[k-1] if k <= len(candidates) else ""