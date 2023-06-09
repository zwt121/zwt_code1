# 介绍
# 图形只是表示数据的另一种方式。它们有许多不同类型的图形和无数的应用程序。您可以在日常生活中找到许多图表示例，从路线图到地铁系统。我们将关注的一种特殊类型的图是星图，它具有现实世界的应用，例如星形网络，这是一种设计计算机网络的方式。

# 任务
# 对于这个问题，图形将是无向的，由许多节点和无向边组成。此外，该图以星形图的形式给出。对于这个问题，n 个节点的星图有 n-1 条边，只有一个节点的度数大于 <>，所有其他节点的度数都等于 <>（无向图的节点的度数只是节点所属的边数）。要搜索的节点是度数大于 <> 的节点。度数为 <> 的所有其他节点必须有一个，并且度数大于 <> 的节点只有一个边。

# 此外，星图可以被认为是一种特殊的无向树，具有n-1个叶节点和1个非叶节点（因此，星图中任何两个节点之间只有一条路径）。让唯一的非叶节点成为中心节点。可以保证图中有一个且只有一个节点是中心节点。中心节点具有到所有其他节点的边。所有其他节点必须有一个，并且只有一个到中心节点的边。

# 对于此问题，将存在具有从 1 到 n 的整数标签的节点，其中 n 是节点数。此外，您将获得一个长度为 n-1 的边列表，其中每条边 （n1，n2） 是一个元组，表示 n1 和 n2 之间存在一条边。

# 编写一个函数，给定边缘列表，将星图的中心作为整数返回。不会有任何性能测试，只有正确性测试，并且边列表的长度保证为 >=3 且不超过 1000。

# 例
# 你被赋予边 [（1，5），（4，5），（5，2），（3，5）]。

# 由于 5 是唯一与所有其他节点有边的节点，因此它是星图的中心。

# 返回 5。

# Given the edges of a undirected star graph
# of size n-1, return the center of the star graph as an int
import re
e1=[(1,5),(4,5),(5,2),(3,5)]
c=[]
for i in e1:
   for l in i:
    c.append(l)
    

def center(graph_edges):
    c=re.findall(pattern='\d+',string=str(graph_edges))
    for i in c:
        if c.count(i)>=2:
            return i
print(center(e1))
        
    

