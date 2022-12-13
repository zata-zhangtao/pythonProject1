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
    failedNode = []
    atcing = []

    def __init__(self,network,attackFun = 1):
        self.attackFun = attackFun
        self.network = network
        self.atcNode = list(network.nodes)

    def randNodeAtc(self,size):
        self.failedNode.extend(self.atcing)
        self.atcing = []
        self.atcing.append(random.choices(self.atcNode,k = size))
        for i in self.atcing:
            if i in self.atcNode:
                self.atcNode.remove(i)
        return self.atcing


    def select(self,NameFun):
        return




if __name__ =="__main__":
    G = createNetworks.createNetworks(sheetname="Sheet1", filePath="../resource/data/1.xlsx", startCol=3).getNetwork()
    print(G.nodes.values())
    print(len(G.nodes))
    attack1 = attack(G,1)
    print(attack1.randNodeAtc(3))
