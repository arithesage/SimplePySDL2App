from sdl2 import SDL_Texture
from graphic import Graphic



class Sprite:
    def __init__(self, graphic: Graphic) -> None:
        self.set_graphic (graphic)


    def __cached__ (self) -> None:
        self._cached = True


    def is_cached (self) -> bool:
        return self._cached


    def width (self) -> int:
        return self._graphic.width ()


    def height (self) -> int:
        return self._graphic.height ()


    def graphic (self) -> Graphic:
        return self._graphic
    

    def set_graphic (self, graphic: Graphic) -> None:        
        self._graphic = graphic
        self._cached = False