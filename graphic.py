from sdl2 import SDL_Surface




class Graphic:
    """
    Used for store the data of a loaded image
    """
    def __init__(self, path: str, surface: SDL_Surface) -> None:
        self.__path = path
        self.__graphic_data = surface
        self.__width = surface[0].w
        self.__height = surface[0].h    
    

    def graphic_data (self) -> SDL_Surface:
        """
        Returns the image itself
        """
        return self.__graphic_data
    

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
