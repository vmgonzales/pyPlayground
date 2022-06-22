class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        distance, min, minIndex = [], 99999, 99999
        for i in range(len(points)):
            point = points[i]
            if point[0] == x or point[1] ==y:
                curDistance = (abs(x - point[0]) + abs(y - point[1]))
                distance.append(curDistance)
                if curDistance < min:
                    minIndex = i
                    min = curDistance
            else:
                distance.append(99999)
        #print(distance)
        #print(minIndex, min)
        if min == 99999: return -1
        else: return minIndex