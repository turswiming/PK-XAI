import pyqtree
from  typing import TypeVar, Generic, List, Tuple

T = TypeVar('T')
#bbox = Tuple[float, float, float, float]
#bbox = [min_x, min_y, max_x, max_y]
class quad_tree(Generic[T]):
    def __init__(self, bbox:Tuple[float, float, float, float]):
        self.bbox = bbox
        self.index = pyqtree.Index(bbox=bbox)

    def insert(self, item:T, bbox):
        self.index.insert(item=item, bbox=bbox)

    def intersect(self, bbox):
        return self.index.intersect(bbox=bbox)
spindex = pyqtree.Index(bbox=[0, 0, 200, 200])
