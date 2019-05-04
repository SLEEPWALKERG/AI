from math import *
class node:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def Calc_Dist(self, another):
        return sqrt(pow(self.x - another.x, 2) + pow(self.y - another.y, 2))