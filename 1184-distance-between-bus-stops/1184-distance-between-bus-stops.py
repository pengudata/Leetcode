class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        all_distance = sum(distance)
        clockwise = sum(distance[start:destination])
        counterclockwise = all_distance - clockwise
        return min(clockwise, counterclockwise)