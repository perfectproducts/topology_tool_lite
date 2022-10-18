from pydantic import BaseModel 
from typing import List , Dict

# model inspired by https://w3c-lbd-cg.github.io/bot 
class ZoneModel(BaseModel):
    name:str=""
class SpaceModel(ZoneModel):
    space_type:str = "" 
class StoreyModel(ZoneModel):
    has_spaces: List[str] = []   
class BuildingModel(ZoneModel):     
    has_storeys : List[str] = []
class SiteModel(ZoneModel):
    geo_lat: float = 0
    geo_long: float = 0
    geo_alt: float = 0 
    has_buildings: List[str] = []

class TopologyModel(BaseModel): 
    sites: Dict[str, SiteModel] = {}
    buildings: Dict[str, BuildingModel] = {}
    storeys : Dict[str, StoreyModel] = {}


    
