class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            max_gift = max(gifts)
            i = gifts.index(max_gift)
            gifts[i] = int(max_gift ** 0.5)
            k -= 1
        return sum(gifts)