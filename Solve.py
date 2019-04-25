from Main import MAX_DIST
import Node

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
        tmpdict = {}
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
                    tmpdict[i] = k
        tmplst = []
        t = self.destination
        while t in tmpdict:
            tmplst.append(tmpdict[t])
            t = tmpdict[t]
        self.path = tmplst.reverse()
        return dist[self.destination]


    def GetPath(self):
        return self.path

class AStar:
    def __init__(self,start,destination,lst_dis,lst_node):
        self.start = start
        self.destination = destination
        self.lst_dis = lst_dis
        self.lst_node = lst_node
        self.lst_open = []
        self.lst_closed = []

    def GetResult(self):
        isFounded = False
        self.lst_open.append((self.lst_node[self.start],self.lst_dis[self.start][self.destination]))
        while len(self.lst_open) > 0:
            self.MySort()
            tmp = self.lst_open.pop(0)[0]
            self.lst_closed.append(tmp)
            if tmp.GetID() == self.destination:
                isFounded = True
                break
            else:
                for each in tmp.GetLink():
                    #calculate the cost
                    haosanzhi = self.lst_dis[tmp][each.GetID()]+ self.lst_dis[tmp][self.destination]
                    if each in self.lst_open and haosanzhi < self.lst_open[self.lst_open.index(each)][1]:
                        self.lst_open[self.lst_open.index(each)][1] = haosanzhi
                    elif each not in self.lst_open:
                        self.lst_open.append((each, haosanzhi))
                    self.lst_open.append(each)
        return isFounded


    def GetPath(self):
        return self.lst_closed

    def MySort(self):
        self.lst_open.sort(key= lambda x:x[1])

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


