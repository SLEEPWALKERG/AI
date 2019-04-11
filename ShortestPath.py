from Main import MAX_DIST


def ShortestPath_Dijkstra(lst, start, destination):
    dist = []
    for i in range(1000):
        dist.append(lst[start][i])
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
            if lst[k][i] + min < dist[i]:
                dist[i] = min + lst[k][i]
    return dist[destination]
