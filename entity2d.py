from entity import Entity
from graphic import Graphic
from sprite import Sprite
from vector_2d import Vector2D




class Entity2D (Entity):
    def __init__(self, graphic: Graphic) -> None:
        super().__init__()

        self._position = Vector2D ()
        self._rotation = Vector2D ()
        self._scale = Vector2D ()
        self._sprite = Sprite (graphic)
        self._renderable = True


    def hide (self) -> None:
        self._renderable = False

    def is_renderable (self) -> bool:
        return self._renderable

    
    def position (self) -> Vector2D:
        return self._position
    

    def rotation (self) -> Vector2D:
        return self._rotation
    

    def scale (self) -> Vector2D:
        return self._scale
    

    def show (self) -> None:
        self._renderable = True
    

    def sprite (self) -> Sprite:
        return self._sprite
