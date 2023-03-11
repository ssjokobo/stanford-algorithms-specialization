import sys
from random import choice


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
                    graph[u] = [int(edge) for edge in vertex[1:]]
                    
            print(mincut(graph))
            for i in graph:
                print(len(graph[i]))

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
    

def mincut(graph):
    # base case
    while len(graph) > 2:

        # random edge
        u = choice(list(graph.keys()))
        v = choice(graph[u])

        # clear from other nodes
        for i in graph:
            if i != u:
                for n, j in enumerate(graph[i]):
                    if j == u:
                        graph[i][n] = v

        # merge vertices
        for i in graph[u]:
            if i != v:
                graph[v].append(i)
        graph.pop(u)

        # clear self loop
        for i in graph:
            while i in graph[i]:
                graph[i].remove(i)

    return graph

if __name__ == "__main__":
    main()