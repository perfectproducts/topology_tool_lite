from pydantic import BaseModel 
from typing import List , Dict

class GeoLocationModel(BaseModel):
    lat: float 
    lon: float 

class ZoneModel(BaseModel):
    name:str 

class StoreyModel(ZoneModel):
    pass 

class BuildingModel(ZoneModel):
    address:str 
    storeys : Dict[str, StoreyModel]

class SiteModel(ZoneModel):
    geo_location: GeoLocationModel
    buildings: Dict[str, BuildingModel]
class TopologyModel(BaseModel): 
    sites:Dict[str, SiteModel]
    
