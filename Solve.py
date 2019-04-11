from Main import MAX_DIST


class ShortestPath_Dijkstra:
    def __init__(self,start, destination,lst):
        self.start = start
        self.destination = destination
        self.lst = lst
        self.path = []

    def GetResult(self):
        dist = []
        for i in range(1000):
            dist.append(self.lst[self.start][i])
        isshortest = [0] * 1000
        min = MAX_DIST
        k = 0
        for x in range(1000):
            for i in range(1000):
                if isshortest[i] == 1:
                    continue
                if min > dist[i]:
                    min = dist[i]
                    k = i
            isshortest[k] = 1
            for i in range(1000):
                if self.lst[k][i] + min < dist[i]:
                    dist[i] = min + self.lst[k][i]
        return dist[self.destination]


    def GetPath(self):
        return self.path

class AStar:
    def __init__(self,start,destination,lst):
        self.start = start
        self.destination = destination
        self.lst = lst

    def GetResult(self):
        pass

    def GetPath(self):
        pass

class LocalSearch_ClimbMountain:
    def __init__(self,start, destination,lst):
        self.start = start
        self.destination = destination
        self.lst = lst
        self.path = []

    def GetResult(self):
        pass

    def GetPath(self):
        return self.path


class LocalSearch_GA:
    def __init__(self, start, destination, lst):
        self.start = start
        self.destination = destination
        self.lst = lst
        self.path = []

    def GetResult(self):
        pass

    def GetPath(self):
        return self.path


class LocalSearch_SA:
    def __init__(self, start, destination, lst):
        self.start = start
        self.destination = destination
        self.lst = lst
        self.path = []

    def GetResult(self):
        pass

    def GetPath(self):
        return self.path


