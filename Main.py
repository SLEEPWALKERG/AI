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
            dis[a][b] = 0
        else:
            dis[a][b] = lst_node[a].Calc_Dist(lst_node[b])
    f2.close()

def output(lst):
    print("The Path is: {}".format(lst[0]), end='')
    for each in lst[1:]:
        print(">>>{}".format(each), end='')
    print()


if __name__ == '__main__':
    print("Please input the start node number and the end node number split by one space: ", end="")
    start,destination = map(int, input().split())
    Data_Init()

    #dijkstra
    print("ShortestPath-Dijkstra:")
    Solve_Dijkstra = Solve.ShortestPath_Dijkstra(start, destination, dis)
    result_dijkstra = Solve_Dijkstra.GetResult()
    if result_dijkstra != MAX_DIST:
        print("The Result is {}".format(result_dijkstra))
        output(Solve_Dijkstra.GetPath())
    else:
        print("No Path")

    #AStar
    print("AStar:")
    Solve_AStar = Solve.AStar(start,destination,dis)
    result_astar = Solve_AStar.GetResult()
    if result_astar != MAX_DIST:
        print("The Result is {}".format(result_astar))
        output(Solve_AStar.GetPath())
    else:
        print("No Path")

