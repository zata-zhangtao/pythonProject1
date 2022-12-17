# 构造方法__init__(self,network:createNetworks,failedNode:list=None,failedEdge:list=None):
# 包括几种鲁棒性分析方法
# 1.aveCon(self) : 平均顶点连通性
# 2.aveClu(self) : 平均聚类系数
# 3.aveEff(self) : 平均网络效率



# putOutFile（self) : 将所有鲁棒性分析结果输出到文件


import pandas as pd
import networkx as nx
import numpy as np
import createNetworks
import attack
class robustnessAnalysis:


    network = None
    failedNode = None
    failedEdge = None
    putOutFile = pd.DataFrame()

    rob = {}

    def __init__(self,network:createNetworks,failedNode:list=None,failedEdge:list=None):
        self.network = network
        self.failedNode = failedNode
        self.failedEdge = failedEdge

    def aveCon(self):
        # 平均顶点连通性
        self.aveCon = []
        failedNode = None
        failedEdge = None
        if self.failedNode:
            failedNode = self.failedNode.copy()
        if self.failedEdge:
            failedEdge = self.failedEdge.copy()
        graph = self.network.copy()
        if failedEdge and failedNode:
            while failedNode or failedEdge:
                self.aveCon.append(nx.average_node_connectivity(graph))
                if failedEdge:
                    graph.remove_edges_from(failedEdge.pop(-1))
                if failedNode:
                    graph.remove_nodes_from(failedNode.pop(-1))
        else:
            if failedEdge:
                faile = failedEdge
                while faile:
                    self.aveCon.append(nx.average_node_connectivity(graph))
                    graph.remove_edges_from(faile.pop(-1))
                    print(faile)
            else:
                faile = failedNode
                while faile:
                    self.aveCon.append(nx.average_node_connectivity(graph))
                    graph.remove_nodes_from(faile.pop(-1))
                    print(faile)
        self.aveCon.append(0)
        print(self.aveCon)
        self.rob["aveCon"] = self.aveCon
        return self.aveCon

    def aveClu(self):
        # 平均聚类系数
        Metrics = []
        failedNode = None
        failedEdge = None
        if self.failedNode:
            failedNode = self.failedNode.copy()
        if self.failedEdge:
            failedEdge = self.failedEdge.copy()
        graph = self.network.copy()
        if failedEdge and failedNode:
            while failedNode or failedEdge:
                cl = nx.clustering(graph)
                if cl:
                    Metrics.append(np.mean(list(cl.values())))
                else:
                    Metrics.append(0)
                if failedEdge:
                    graph.remove_edges_from(failedEdge.pop(-1))
                if failedNode:
                    graph.remove_nodes_from(failedNode.pop(-1))
        else:
            if failedEdge:
                faile = failedEdge
                while faile:
                    cl = nx.clustering(graph)
                    if cl:
                        Metrics.append(np.mean(list(cl.values())))
                    else:
                        Metrics.append(0)
                    graph.remove_edges_from(faile.pop(-1))
                    print(faile)
            else:
                faile = failedNode
                while faile:
                    cl = nx.clustering(graph)
                    if cl:
                        Metrics.append(np.mean(list(cl.values())))
                    else:
                        Metrics.append(0)
                    graph.remove_nodes_from(faile.pop(-1))
                    print(faile)
        Metrics.append(0)
        print(Metrics)
        self.rob["aveClu"] = Metrics
        return Metrics
    def aveEff(self):
        # 平均网络效率
        Metrics = []
        failedNode = None
        failedEdge = None
        graph = self.network.copy()
        N = len(graph.nodes)
        if self.failedNode:
            failedNode = self.failedNode.copy()
        if self.failedEdge:
            failedEdge = self.failedEdge.copy()

        if failedEdge and failedNode:
            while failedNode or failedEdge:
                eff = 0
                for i in graph.nodes:
                    for j in graph.nodes:
                        if i != j:
                            eff = nx.shortest_path_length(G,source =i, target=j, weight ='weight') + eff
                if eff:
                    Metrics.append(eff/(N*(N-1)))
                else:
                    Metrics.append(0)
                if failedEdge:
                    graph.remove_edges_from(failedEdge.pop(-1))
                if failedNode:
                    graph.remove_nodes_from(failedNode.pop(-1))
        else:
            if failedEdge:
                faile = failedEdge
                while faile:
                    eff = 0
                    for i in graph.nodes:
                        for j in graph.nodes:
                            if i != j:
                                eff = nx.shortest_path_length(G, source=i, target=j, weight='weight') + eff
                    if eff:
                        Metrics.append(eff/(N*(N-1)))
                    else:
                        Metrics.append(0)
                    graph.remove_edges_from(faile.pop(-1))
                    print(faile)
            else:
                faile = failedNode
                while faile:
                    eff = 0
                    for i in graph.nodes:
                        for j in graph.nodes:
                            if i != j:
                                eff = nx.shortest_path_length(G, source=i, target=j, weight='weight') + eff
                    if eff:
                        Metrics.append(eff/(N*(N-1)))
                    else:
                        Metrics.append(0)
                    graph.remove_nodes_from(faile.pop(-1))
                    print(faile)
        Metrics.append(0)
        self.rob["aveClu"] = Metrics
        return Metrics
    def putOutFile(self):
        return
if __name__ == "__main__":
    # 创建网络
    G = createNetworks.createNetworks(sheetname="Sheet1", filePath="../resource/data/1.xlsx", startCol=3).getNetwork()
    # 创建攻击模式，并获得攻击顺序
    attack1 = attack.attack(G, 1).randNodeAtc(size=3)
    # randEdgeList = attack.attack(G,1).ranEdgeAtc(size = 6)

    rob = robustnessAnalysis(network=G,failedNode=attack1)
    # robRandEdge = robustnessAnalysis(network=G,failedNode=attack1, failedEdge=randEdgeList).aveCon()
    # robRandEdgeclu = robustnessAnalysis(network=G,failedNode=attack1)
    # robRandEdgeclu.aveCon()
    # print(robRandEdgeclu.rob)
    rob.aveEff()
    print(rob.rob)


