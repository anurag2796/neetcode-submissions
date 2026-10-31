class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = sorted(zip(position, speed), key=lambda pair: pair[0], reverse=True)
        
        # position_tuple, speed_tuple = zip(*pairs)
        # position = list(position_tuple)
        # speed = list(speed_tuple)

        # if len(speed) == 0:
        #     return 0

        pos, spd = map(list, zip(*pairs))
        time = (target - pos[0]) / spd[0]
        count = 1
        for i in range(1, len(pos)):
            temp = (target - pos[i]) / spd[i]
            if time < temp:
                time = temp
                count +=1


        return count
                    
                 

            