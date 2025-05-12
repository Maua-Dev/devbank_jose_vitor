from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.item_type_enum import ItemTypeEnum

from ..entities.item import Item


class IItemRepository(ABC):
    
    
    @abstractmethod
    def get_all_items(self) -> List[Item]:
        
        pass
    
    @abstractmethod
    def get_item(self, item_id: int) -> Optional[Item]:
        
        pass
    
    @abstractmethod
    def create_item(self, item: Item, item_id: int) -> Item:
        
        pass
    
    @abstractmethod
    def delete_item(self, item_id: int) -> Item:
        pass
        
    @abstractmethod
    def update_item(self, item_id:int, name:str=None, price:float=None, item_type:ItemTypeEnum=None, admin_permission:bool=None) -> Item:
        
        pass
    
    