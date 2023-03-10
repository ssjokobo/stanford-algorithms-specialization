import sys


def main():

    # check argv
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".txt"):
        sys.exit("Must be a .txt file")
    else:
        try:
            graph = dict()
            with open(sys.argv[1]) as file:
                for line in file:
                    vertex = line.strip().split("\t")
                    u = int(vertex[0])
                    graph[u] = dict()
                    for edge in vertex[1:]:
                        m, n = edge.split(",")
                        m = int(m)
                        n = int(n)
                        graph[u][m] = n
            
            shortest_path = dijkstra(graph, 1)
            path_cost = [shortest_path[i - 1][1] for i in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]]
            print(path_cost)

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


def dijkstra(graph, start):
    X = [start]
    V = list(graph.keys())
    A = {start: 0}
    
    while X != V:
        
        costs = dict()
        for v in X:
            for w in graph[v]:
                if w not in X:
                    costs[(v, w)] = A[v] + graph[v][w]
                    
        if len(costs) > 0:
            costs = sorted(costs.items(), key=lambda x:x[1])
            X.append(costs[0][0][1])
            A[costs[0][0][1]] = costs[0][1]
        else:
            break
    
    A = sorted(A.items(), key=lambda x:x[0])
    return A


if __name__ == "__main__":
    main()