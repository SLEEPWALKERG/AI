from Node import *
import Solve

lst_node = []
MAX_DIST = 10000000
dis = [([MAX_DIST] * 1000) for i in range(1000)]


def Data_Init():
    f1 = open("city.txt", encoding="utf-8")
    i = 0
    for each in f1.readlines():
        tmp = each.split()
        lst_node.append(node(float(tmp[1]), float(tmp[2]), i))
        i += 1
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
    f2.close()


if __name__ == '__main__':
    start,destination = map(int, input().split())
    Data_Init()

    #dijkstra
    print("ShortestPath-Dijkstra:")
    Solve_Dijkstra = Solve.ShortestPath_Dijkstra(start, destination, dis)
    result_dijkstra = Solve_Dijkstra.GetResult()
    if result_dijkstra != MAX_DIST:
        print("The Result is {}".format(result_dijkstra))
        print("The Path is: {}".format(start), end='')
        path_dijkstra = Solve_Dijkstra.GetPath()
        if path_dijkstra is not None:
            for each in Solve_Dijkstra.GetPath():
                print(">>>{}".format(each), end='')
        print(">>>{}".format(destination))
    else:
        print("No Path")

    #AStar
    #Solve.AStar(0,814,dis,lst_node).GetResult()
