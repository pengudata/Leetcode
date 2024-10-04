class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        answer = 0
        prev = 0
        for upper, percent in brackets:
            if income <= prev:
                break
            taxable_income = min(income, upper) - prev
            answer += taxable_income * (percent / 100)
            prev =  upper
        return answer