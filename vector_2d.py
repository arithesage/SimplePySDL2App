

class Vector2D:
    """
    A two components float vector
    """
    def __init__(self, 
                 x: float = 0.0,
                 y: float = 0.0 ) -> None:
        
        self.__x = 0.0
        self.__y = 0.0    


    def dec (self, amount: float) -> None:
        """
        Decrements both components
        """
        self.dec_x (amount)
        self.dec_y (amount)


    def dec_x (self, amount: float) -> None:
        """
        Decrements X
        """
        self.__x -= amount


    def dec_y (self, amount: float) -> None:
        """
        Decrements Y
        """
        self.__y -= amount


    def inc (self, amount: float) -> None:
        """
        Increments both components
        """
        self.inc_x (amount)
        self.inc_y (amount)
        

    def inc_x (self, amount: float) -> None:
        """
        Increments X
        """
        self.__x += amount


    def inc_y (self, amount: float) -> None:
        """
        Increments Y
        """
        self.__y += amount


    def set (self, x: float, y: float) -> None:
        """
        Set both components values
        """
        self.__x = x
        self.__y = y


    def set_x (self, x: float) -> None:
        """
        Sets X value
        """
        self.__x = x


    def set_y (self, y: float) -> None:
        """
        Sets Y value
        """
        self.__y = y


    def x (self) -> float:
        """
        Returns X
        """
        return self.__x
    

    def y (self) -> float:
        """
        Returns Y
        """
        return self.__y
        