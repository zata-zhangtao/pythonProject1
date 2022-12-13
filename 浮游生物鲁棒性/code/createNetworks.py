import pandas as pd
import networkx as nx
class createNetworks:
    def __init__(self,filePath):
        self.data = pd.read_excel(filePath)
    # def networks(self):

