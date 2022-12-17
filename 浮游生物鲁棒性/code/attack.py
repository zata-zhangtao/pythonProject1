import math
import random
import networkx as nx
import createNetworks


class attack:
    attackFun = None  # 鲁棒性分析攻击方式
    modelList ={
    "1": "randNodeAtt",
    "2": "random Node Attack"
    }
    network = None #createNetworkx对象
    atcNode = []
    atcEdge = []
    failedNode = []
    failedEdge = []
    atcing = []

    # 攻击顺序列表字典
    atc = {}
    def __init__(self,network):
        self.network = network
        self.atcNode = list(network.nodes)
        self.atcEdge = list(network.edges)

    def randNodeAtc(self,size,step=None):
        #随机顶点攻击

        graph = self.network.copy()
        if step:
            if step > len(graph.nodes()):
                print("step过大")
                return
            size = math.floor(len(graph.nodes) / step)

        if self.atcing:
            self.failedNode.append(self.atcing)
        while len(self.atcNode)>size:
            self.atcing = []
            for i in range(size):
                remove = random.choice(self.atcNode)
                self.atcing.append(remove)
                self.atcNode.remove(remove)
            self.failedNode.append(self.atcing)
        self.failedNode.append(self.atcNode)
        self.atc["randNodeAtc"] = self.failedNode
        return self.failedNode

    def ranEdgeAtc(self,size,step=None):

        # 随机边攻击
        graph = self.network.copy()
        if step:
            if step > len(graph.nodes()):
                print("step过大")
                return
            size = math.floor(len(graph.nodes) / step)

        if self.atcing:
            self.failedEdge.append(self.atcing)
        while len(self.atcEdge) > size:
            self.atcing = []
            for i in range(size):
                remove = random.choice(self.atcEdge)
                self.atcing.append(remove)
                self.atcEdge.remove(remove)
            self.failedEdge.append(self.atcing)
        self.failedEdge.append(self.atcEdge)
        self.atc["ranEdgeAtc"] = self.failedEdge
        return self.failedEdge

    def nodeBetAtc(self,size=None,step=None):
        # 优先看step

        # 基于顶点介数中心性的攻击
        graph  = self.network.copy()
        if step:
            if step > len(graph.nodes()):
                print("step过大")
                return
            size = math.floor(len(graph.nodes)/step)

        bet = nx.betweenness_centrality(graph)
        bet = sorted(bet.items(),key= lambda x:x[1],reverse=True)
        failedList = []
        for i in bet:
            failedList.append(i[0])
        failedNode = []
        while len(failedList) > size:
            failed = []
            for i in range(size):
                failed.append(failedList.pop(-1))
            failedNode.append(failed)
        failedNode.append(failedList)
        self.atc["nodeBetAtc"] = failedNode
        return failedNode

    def edgeBetAtc(self,size = None,step = None):

        # 基于顶点介数中心性的攻击
        graph = self.network.copy()
        if step:
            if step > len(graph.edges()):
                print("step过大")
                return
            size = math.floor(len(graph.edges()) / step)
        bet = nx.edge_betweenness_centrality(graph)
        bet = sorted(bet.items(), key=lambda x: x[1], reverse=True)

        # 判断是是否出错
        if len(bet) != len(graph.edges):
            print("wrong")
        failedList = []
        for i in bet:
            failedList.append(i[0])
        failed = []
        while len(failedList) > size:
            faile = []
            for i in range(size):
                faile.append(failedList.pop(-1))
            failed.append(faile)
        failed.append(failedList)
        self.atc["edgeBetAtc"] = failed
        return failed
    def weightClo(self,size=None,step=None):
        graph = self.network.copy()
        if step:
            if step > len(graph.edges()):
                print("step过大")
                return

        atcList ={}
        for i in graph.nodes:
            cloForK = 0
            for j in graph.nodes:
                cloForK += nx.shortest_path_length(graph,source=i,target=j,weight='weight')
            atcList[i]=cloForK
        atcList = sorted(atcList.items(),key=lambda x:x[1],reverse=True)
        temp = []
        for i in atcList:
            temp.append(i[0])
        failedList = temp

        # 判断是是否出错
        if len(atcList) != len(graph.nodes):
            print("wrong")
        failed = []
        while len(failedList) > size:
            faile = []
            for i in range(size):
                faile.append(failedList.pop(-1))
            failed.append(faile)
        failed.append(failedList)
        print("******attack_weightClo:\n",failed)
        self.atc["weightClo"] = failed
        return failed


    def select(self,NameFun):
        return




if __name__ =="__main__":
    # 创建网络
    G = createNetworks.createNetworks(sheetname="Sheet1", filePath="../resource/data/1.xlsx", startCol=3).getNetwork()
    # 创建攻击对象（attack对象）
    attack = attack(G)

    # print("网络节点列表： ",G.nodes.values())
    # print("网络节点列表长度： ",len(G.nodes))
    # #创建attack对象
    # attack1 = attack(G,1)
    # # 随机节点攻击
    # failList = attack1.randNodeAtc(3)
    # nodeAtcSize = 3
    # print("随机节点攻击，每次攻击节点数",nodeAtcSize," ,受攻击列表： ",failList)
    # print("受攻击列表长度 ：",len(failList))
    #
    # # 随机边攻击
    # edgeAtcSize = 6
    # faileEdgelist = attack1.ranEdgeAtc(size=edgeAtcSize)
    # print("随机边攻击，每次攻击边数",edgeAtcSize,"受攻击列表",faileEdgelist)
    # print("受攻击列表长度 ：",len(faileEdgelist))

    #点介中心性攻击
    # attack.nodeBetAtc(size=3,step=5)

    # 边介中心性攻击
    # attack.edgeBetAtc(size=3,step=22)

    # 权重接近中心性
    attack.weightClo(size=3)
