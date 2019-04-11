from Node import *
import numpy as np
import ShortestPath

lst_node = []
MAX_DIST = 100000
#dist = np.full((1000, 1000), MAX_DIST, dtype=float)
dist = [[MAX_DIST] * 1000] * 1000


def func():
    x1 = node(3,2)
    x2 = node(2,3)
    print(x1.Calc_Dist(x2))

def Data_Init():
    f1 = open("city.txt", encoding="utf-8")
    for each in f1.readlines():
        tmp = each.split()
        lst_node.append(node(float(tmp[1]),float(tmp[2])))
    f1.close()
    f2 = open("link.txt", encoding="utf-8")
    for each in f2.readlines():
        tmp = each.split()
        a = int(tmp[0])
        b = int(tmp[1])
        if a == b:
            continue
        lst_node[a].lst_link.append(b)
        lst_node[b].lst_link.append(a)
        dist[a][b] = lst_node[a].Calc_Dist(lst_node[b])
        dist[b][a] = lst_node[a].Calc_Dist(lst_node[b])

if __name__ == '__main__':
    #func()
    for i in range(1000):
        print(dist[0][i])
    Data_Init()
    '''for each in lst_node:
        print(each.lst_link)'''
    for i in range(1000):
        print(dist[0][i])
    ShortestPath.ShortestPath_Dijkstra(dist, 0, 100)
