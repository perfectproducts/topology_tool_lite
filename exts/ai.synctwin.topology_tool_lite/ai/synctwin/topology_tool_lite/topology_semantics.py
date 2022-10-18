from ai.synctwin.topology_tool_lite.topology_model import TopologyModel


from .topology_model import TopologyModel
from pxr import Usd, Sdf

class TopologySemantics:
    DEFAULT_ROOT_PATH = "/World/topology"
    def write(self, stage:Usd.Stage, topology:TopologyModel, prim_path:str=""):        
        root_path = TopologySemantics.DEFAULT_ROOT_PATH if prim_path == "" else prim_path
        stage.RemovePrim(root_path)
        topo_prim = stage.DefinePrim(root_path, "Xform")
        
        topo_prim.CreateAttribute("mfgstd:schema", Sdf.ValueTypeNames.String).Set("SiteTopology#1.0.0") 
