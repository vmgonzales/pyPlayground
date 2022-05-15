class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) == 2: return True
        
        c = coordinates
        rise = c[1][1] - c[0][1]
        run = c[1][0] - c[0][0]
        if run == 0: slope = 99999
        else: slope = rise / run
        #print(rise, run, slope)
        
        for i in range (2, len(c)):
            nextRise = c[i][1] - c[i-1][1]
            nextRun = c[i][0] - c[i-1][0]
            if nextRun == 0: nextSlope = 99999
            else: nextSlope = nextRise / nextRun
            if nextSlope != slope: return False
        
        return True