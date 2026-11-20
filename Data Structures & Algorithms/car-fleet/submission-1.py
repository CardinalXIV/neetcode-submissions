class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # combine both car position and speed into a single list
        # sort reverse so nearest car is infront
        cars = sorted(zip(position, speed), reverse = True)
        fleets = 0
        slowest_time = 0.0 #float for division

        for position, speed in cars:
            time = (target - position) / speed
    
            # check fleet ahead speed
            # cannot catch up start a new fleet and record time
            if slowest_time < time:
                slowest_time = time
                fleets += 1
        

        return fleets