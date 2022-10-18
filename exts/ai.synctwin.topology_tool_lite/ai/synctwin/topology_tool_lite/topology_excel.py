import pandas as pd
from .topology_model import TopologyModel
class TopologyExcelReaderWriter:

    def read(self, xls_path: str) -> TopologyModel:
        
        topology= TopologyModel()

        return topology 


    def write(self, xls_path: str, topology : TopologyModel):
        # not implemented in lite 
        pass 

