class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        answer = 0
        seats = sorted(seats)
        students = sorted(students)
        for seat, student in zip(seats, students):
            answer += abs(seat - student)
        return answer