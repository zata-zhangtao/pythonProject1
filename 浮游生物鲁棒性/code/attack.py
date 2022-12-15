import random

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

    def __init__(self,network,attackFun = 1):
        self.attackFun = attackFun
        self.network = network
        self.atcNode = list(network.nodes)
        self.atcEdge = list(network.edges)

    def randNodeAtc(self,size):
        #随机顶点攻击
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
        return self.failedNode


    def ranEdgeAtc(self,size):
        # 随机边攻击
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
        return self.failedEdge


    def select(self,NameFun):
        return




if __name__ =="__main__":
    # 创建网络
    G = createNetworks.createNetworks(sheetname="Sheet1", filePath="../resource/data/1.xlsx", startCol=3).getNetwork()
    print("网络节点列表： ",G.nodes.values())
    print("网络节点列表长度： ",len(G.nodes))
    #创建attack对象
    attack1 = attack(G,1)
    # 随机节点攻击
    failList = attack1.randNodeAtc(3)
    nodeAtcSize = 3
    print("随机节点攻击，每次攻击节点数",nodeAtcSize," ,受攻击列表： ",failList)
    print("受攻击列表长度 ：",len(failList))

    # 随机边攻击
    edgeAtcSize = 6
    faileEdgelist = attack1.ranEdgeAtc(size=edgeAtcSize)
    print("随机边攻击，每次攻击边数",edgeAtcSize,"受攻击列表",faileEdgelist)
    print("受攻击列表长度 ：",len(faileEdgelist))
