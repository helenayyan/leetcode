# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        pass

class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x1, y1 = topRight.x, topRight.y
        x2, y2 = bottomLeft.x, bottomLeft.y

        if x1 < x2 or y1 < y2 or not sea.hasShips(topRight, bottomLeft):
            return 0

        if x1 == x2 and y1 == y2:
            return 1

        x_mid = (x1 + x2) // 2
        y_mid = (y1 + y2) // 2

        # consider boarder only once
        return self.countShips(sea, topRight, Point(x_mid + 1, y_mid + 1)) + self.countShips(sea, Point(x_mid, y_mid),
                                                                                             bottomLeft) + self.countShips(
            sea, Point(x1, y_mid), Point(x_mid + 1, y2)) + self.countShips(sea, Point(x_mid, y1), Point(x2, y_mid + 1))
