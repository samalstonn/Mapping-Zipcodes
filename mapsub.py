"""
Subcontroller for map.py containing the map objects and pin objects
"""

from game2d import *
from mapconsts import *

class WorldMap(GImage):
    """
    World map image class
    """

    def __init__(self,x,y,width,height,source):
        """
        Inits the world map image with the given parameters
        """
        super().__init__(x=x,y=y,width=width,height=height,source=source)

class Pin(GImage):
    """
    Pin image class
    """

    def __init__(self,x,y,width,height,source,type):
        """
        Inits the Pin image with the given parameters

        Parameter type: color of the pin
        Precondition: type is a string either 'red','blue','green','black',
                      or 'orange'
        """
        super().__init__(x=x,y=y,width=width,height=height,source=source)
        self._type = type
        self.detType()

    def detType(self):
        """
        Determines the type of pin to use
        """
        if self._type == 'blue':
            self.source = 'bluepin.png'
        elif self._type == 'red':
            self.source = 'redpin.png'
        elif self._type == 'orange':
            self.source = 'orangepin.png'
        elif self._type == 'green':
            self.source = 'greenpin.png'
        elif self._type == 'black':
            self.source = 'blackpin.png'
