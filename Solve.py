from Main import MAX_DIST
import Node
import time


class ShortestPath_Dijkstra:
    def __init__(self, start, destination, lst_dis):
        self.start = start
        self.destination = destination
        self.lst_dis = lst_dis
        self.path = []

    def GetResult(self):
        begin = time.time()
        tmpdict = {}  # To store the information of father node
        dist = []  # To store the information about the distance of all the other nodes to the start node
        for i in range(1000):
            if self.lst_dis[self.start][i] != MAX_DIST:
                tmpdict[i] = self.start
            dist.append(self.lst_dis[self.start][i])
        isshortest = [0] * 1000
        isshortest[self.start] = 1
        isshortest[self.destination] = 1
        k = 0
        for x in range(1000):  # The process of dijkstra
            min = MAX_DIST
            for i in range(1000):
                if isshortest[i] == 1:
                    continue
                if min > dist[i]:
                    min = dist[i]
                    k = i
            isshortest[k] = 1
            for i in range(1000):
                if self.lst_dis[k][i] + min < dist[i]:
                    dist[i] = min + self.lst_dis[k][i]
                    tmpdict[i] = k
        # Get the answer path
        tmplst = []
        t = self.destination
        tmplst.append(t)
        while t in tmpdict and t != self.start:
            tmplst.append(tmpdict[t])
            t = tmpdict[t]
        tmplst.reverse()
        self.path = tmplst
        end = time.time()
        print("The time Dijkstra takes is: {}".format(end - begin))
        return dist[self.destination]

    def GetPath(self):
        return self.path


class AStar:
    def __init__(self, start, destination, lst_dis):
        self.start = start
        self.destination = destination
        self.lst_dis = lst_dis
        self.lst_open = []
        self.lst_closed = []
        self.path = []

    # the type of open table is [[node number, cost],[node number, cost]......]
    def GetResult(self):
        begin = time.time()
        isFounded = MAX_DIST
        if self.start == self.destination and self.lst_dis[self.start][self.destination] == 0:
            isFounded = 0
        dic = {}  # To store the information of father node
        isopen = [0] * 1000  # To store the information whether the node is in open table
        self.lst_open.append([self.start, self.lst_dis[self.start][self.destination]])  # initialize the open table
        while len(self.lst_open) > 0:  # if the open table is empty, break
            self.MySort()  # To sort the open table in order to get the node of the lowest cost
            tmp = self.lst_open.pop(0)
            if tmp[0] == self.destination:
                break
            self.lst_closed.append(tmp[0])
            for i in range(1000):
                if i in self.lst_closed:
                    continue
                tmpdis = self.lst_dis[tmp[0]][i]
                if tmpdis != MAX_DIST:
                    x = tmp[0]
                    while x != self.start and x in dic:
                        tmpdis += self.lst_dis[dic[x]][x]
                        x = dic[x]
                    # tmpdis refers to the distance from the start node to the current node
                    cost = tmpdis + self.lst_dis[i][self.destination]  # Calculate the cost
                    if isopen[i] == 0:  # if the current node number isn't in the open table, add it
                        self.lst_open.append([i, cost])
                        isopen[i] = 1
                        dic[i] = tmp[0]
                    else:  # Else if the cost is smaller, update it
                        for each in self.lst_open:
                            if each[0] == i:
                                if each[1] > cost:
                                    each[1] = cost
                                    dic[i] = tmp[0]
                                break
        # Get the answer path
        tmplst = [self.destination]
        t = self.destination
        if t in dic:
            isFounded = 0
        while t in dic:
            tmplst.append(dic[t])
            isFounded += self.lst_dis[dic[t]][t]
            t = dic[t]
        tmplst.reverse()
        self.path = tmplst
        end = time.time()
        print("The time AStar takes is: {}".format(end - begin))
        return isFounded

    def GetPath(self):
        return self.path

    def MySort(self):
        self.lst_open.sort(key=lambda x: x[1])


class LocalSearch_ClimbMountain:
    def __init__(self, start, destination, lst):
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
