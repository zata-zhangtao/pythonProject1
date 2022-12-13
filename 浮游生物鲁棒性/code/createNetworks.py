import pandas as pd
import networkx as nx
import scipy.stats as ss
class createNetworks:
    data = None  #导入的文件数据
    network = nx.Graph() #创建的网络
    ccf = None #相关系数数组

    def __init__(self,filePath,sheetname,startCol = 0):
        self.data = pd.read_excel(filePath,sheet_name=sheetname).iloc[:,startCol:]


    def computeCorrelationCoefficient(self):
        #colName  #列表名数组变量
        #cof #相关系数变量


        colName = self.data.columns.values
        self.ccf = pd.DataFrame(index= colName,columns= colName)
        for i in colName:
            for j in colName:
                cof = ss.spearmanr(self.data.loc[:,i],self.data.loc[:,j])
                if cof[1]<0.05:
                    self.ccf.loc[i][j] = cof[0]
        return self.ccf

    def getNetwork(self):
        colName = self.data.columns.values
        self.network.add_nodes_from(colName)
        self.ccf = pd.DataFrame(index=colName, columns=colName)
        x = 0
        for i in colName:
            for j in colName:
                cof = ss.spearmanr(self.data.loc[:, i], self.data.loc[:, j])
                if cof[1] < 0.05:
                    if i != j :
                        x += 1
                        self.network.add_edge(i,j)
                        self.ccf.loc[i][j] = cof[0]
        graph = self.network.copy()
        self.network.remove_nodes_from(nx.isolates(graph))
        return self.network
    def PrintData(self):
        print("data")
        print(self.data)
        print("ccf")
        print(self.ccf)


if __name__ == '__main__':
    G = createNetworks(sheetname="Sheet1", filePath="../resource/data/1.xlsx",startCol=3).getNetwork()
    print(len(G.nodes))
    print(len(G.edges))



