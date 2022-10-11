"""
Creates a Map from excel data
"""

from game2d import *
from mapconsts import *
from mapsub import *
import math
import pgeocode as pg

class Map(GameApp):
    """
    Map controller
    """

    def start(self,pinlist):
        """
        """
        self._state = STATE_BEGIN
        self._pinlist = []
        self.setMap()
        self.setPins(pinlist)



    def update(self,dt):
        """
        """
        # self.draw()


    def draw(self):
        """
        """
        if self._state == STATE_BEGIN:
            self._map.draw(self.view)
            for pin in self._pinlist:
                pin.draw(self.view)

    def setMap(self):
        """
        Sets Map
        """
        self._map = WorldMap(x=MAP_X,y=MAP_Y,width=MAP_WIDTH,
                             height=MAP_HEIGHT,source=MAP_SOURCE)

    def setPins(self,pinlist):
        """
        Sets the Pin objects from the pinlist
        """
        long = 0
        g=0
        x=0
        colors = ['red','blue','green']
        for pin in pinlist:
            if not g==10:
                print(pinlist.index(pin))
                nomi = pg.Nominatim('us')
                lat = float(nomi.query_postal_code(pin).latitude)
                long = float(nomi.query_postal_code(pin).longitude)
                piny = (MAP_WIDTH/(2*math.pi))*(math.log(math.tan((math.pi/4)+(lat/2)*(math.pi/180))))
                piny += MAP_HEIGHT/2
                pinx = (long + 180) * (MAP_WIDTH / 360)
                # piny = (lat + 180) * (MAP_HEIGHT / 360)
                pin = Pin(x=pinx,y=piny,width=5,height=5,
                                source='bluepin.png',type=colors[x])
                self._pinlist.append(pin)
                g+=1
                if not x==2:
                    x+=1
                else:
                    x=0
        print(self._pinlist)

if __name__ == '__main__':
    Map(width=GAME_WIDTH,height=GAME_HEIGHT,pinlist=['07719','35004']).run()
