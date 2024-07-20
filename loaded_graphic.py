from sdl2 import SDL_Surface




class LoadedGraphic:
    """
    Used for store the data of a loaded image
    """
    def __init__(self, path: str, graphic: SDL_Surface) -> None:
        self.__path = path
        self.__graphic = graphic
        self.__width = graphic[0].w
        self.__height = graphic[0].h    
    

    def graphic (self) -> SDL_Surface:
        """
        Returns the image itself
        """
        return self.__graphic
    

    def path (self) -> str:
        """
        Returns the image file path
        """
        return self.__path
    

    def width (self) -> int:
        """
        Returns the image width
        """
        return self.__width
    

    def height (self) -> int:
        """
        Returns the image height
        """
        return self.__height
