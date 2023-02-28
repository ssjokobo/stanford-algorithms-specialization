import sys
import threading

T = 0
S = None

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
            # [0] = visited 
            # [1] = leader
            # [2] = edges
            # [3] = finishing time
            # [4] = score
            rgraph = dict()

            with open(sys.argv[1]) as file:
                for line in file:
                    u, v = line.strip().split(" ")

                    if int(u) not in graph:
                        graph[int(u)] = [False, None, [int(v)], 0, 0]
                    elif int(v) != int(u) and int(v) not in graph[int(u)][2]:
                        graph[int(u)][2].append(int(v))

                    if int(v) not in rgraph:
                        rgraph[int(v)] = [False, None, [int(u)], 0, 0]
                    elif int(u) != int(v) and int(u) not in rgraph[int(v)][2]:
                        rgraph[int(v)][2].append(int(u))


            # reversed nodes list
            rev_nodes = list(rgraph.keys())

            # kosaraju first loop
            dfsloop(rgraph, rev_nodes)

            # finishing time nodes list
            fin_nodes = [{"id": i, "fintime": rgraph[i][3]} for i in list(rgraph.keys())]
            fin_nodes.sort(reverse=True, key=get_fin_time)
            sorted_nodes = [fin_nodes[i]["id"] for i in range(len(fin_nodes))]
            
            # Kosaraju second loop
            dfsloop(graph, sorted_nodes)
            
            # scoring
            for i in graph:
                try:
                    graph[graph[i][1]][4] += 1
                except KeyError:
                    continue

            scores = []
            for i in graph:
                scores.append(graph[i][4])

            scores.sort()
            scores.reverse()

            print(scores[:5])

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


def get_fin_time(cell):
    return cell["fintime"]
    

def dfsloop(graph, nodes):
    global T, S
    
    T = 0
    S = None

    for i in nodes:
        try:
            if not graph[i][0]:
                S = i
                dfs(graph, i)
        except KeyError:
            continue


def dfs(graph, i):
    global T, S

    graph[i][0] = True
    graph[i][1] = S

    for j in graph[i][2]:
        try:
            if not graph[j][0]:
                dfs(graph, j)
        except KeyError:
            continue
    
    T += 1
    graph[i][3] = T


if __name__ == "__main__":
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=main)
    thread.start()