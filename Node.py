from math import *
class node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lst_link = []

    def Calc_Dist(self, another):
        return sqrt(pow(self.x - another.x, 2) + pow(self.y - another.y, 2))