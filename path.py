import sys
from collections import defaultdict

def driver():
    numGraphs = int(sys.stdin.readline())
    for c in range(numGraphs):
        print("\nGraph Number: {}".format(c+1))
        numNodes = int(sys.stdin.readline())
        numEdges = int(sys.stdin.readline())
        graph = {n: [] for n in range(1,numNodes)}
        for e in range(numEdges):
            outNode,inNode = sys.stdin.readline().strip().split()
            graph[int(outNode)].append(int(inNode))

        numPath = [None]*(numNodes+1)                                   #initialization
        longestPath = [None]*(numNodes+1)
        shortestPath = [None]*(numNodes+1)
        for i in range(2,numNodes+1):
            numPath[i] = 0
            longestPath[i] = 0
            shortestPath[i] = sys.float_info.max
        numPath[1] = 1
        longestPath[1] = 0
        shortestPath[1] = 0

        for i in range(1,numNodes):                                     #BFS search
            for j in graph[i]:
                if(j in graph[i]):
                    numPath[j] = numPath[i]+numPath[j]
                    longestPath[j] = max(longestPath[j], longestPath[i]+1)
                    shortestPath[j] = min(shortestPath[j], shortestPath[i]+1)

        print("Shortest paths is: {}".format(shortestPath[-1]))
        print("Longest paths is: {}".format(longestPath[-1]))
        print("Number of paths is: {}".format(numPath[-1]))



# call with Python 3
if __name__ == "__main__":                            #sets driver as __main__
    driver()
