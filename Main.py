from Node import *
import ShortestPath

lst_node = []
MAX_DIST = 100000
dis = [([MAX_DIST] * 1000) for i in range(1000)]


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
        dis[a][b] = lst_node[a].Calc_Dist(lst_node[b])
        dis[b][a] = lst_node[a].Calc_Dist(lst_node[b])

if __name__ == '__main__':
    Data_Init()
    answer = ShortestPath.ShortestPath_Dijkstra(dis, 0, 345)
    print(answer)
