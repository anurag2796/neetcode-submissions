class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # zip(position, speed) pairs items at matching indexes:
        # position = [10, 8, 0], speed = [2, 4, 1]
        # -> (10, 2), (8, 4), (0, 1)
        #
        # key=lambda pair: pair[0] tells sorted() to compare each pair
        # using its first element—the position, not the speed.
        # lambda pair: pair[0] is a short function equivalent to:
        # def get_position(pair):
        #     return pair[0]
        #
        # reverse=True sorts positions from highest to lowest,
        # so we process cars closest to the target first.
        pairs = sorted(
            zip(position, speed),
            key=lambda pair: pair[0],
            reverse=True
        )

        # *pairs unpacks the pairs as separate arguments to zip():
        # zip(*[(10, 2), (8, 4), (0, 1)])
        # is equivalent to zip((10, 2), (8, 4), (0, 1)).
        #
        # zip then groups matching indexes from those tuples:
        # -> (10, 8, 0) and (2, 4, 1)
        #
        # map(list, ...) applies list() to each resulting tuple:
        # -> [10, 8, 0] and [2, 4, 1]
        #
        # Assignment unpacks those two lists into pos and spd.
        pos, spd = map(list, zip(*pairs))

        time = (target - pos[0]) / spd[0]
        count = 1

        for i in range(1, len(pos)):
            temp = (target - pos[i]) / spd[i]
            if time < temp:
                time = temp
                count += 1

        return count