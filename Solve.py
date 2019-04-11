from Main import MAX_DIST


class ShortestPath_Dijkstra:
    def __init__(self,start, destination,lst):
        self.start = start
        self.destination = destination
        self.lst = lst

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
