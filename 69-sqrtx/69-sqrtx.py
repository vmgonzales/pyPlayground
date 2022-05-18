class Solution:
    def mySqrt(self, x: int) -> int:
        # Test and handle boundary cases
        if x == 0: return 0
        
        guess = 5
        err = 999999.9
        last = 99999
        while abs(err) > .5:
            last = guess
            guess += .000001
            guess = (guess + x / guess) / 2
            err = guess - last
            
            # Print statement for debugging
            #print(x, sqrt(x), guess, err)
        return int(math.floor(guess))