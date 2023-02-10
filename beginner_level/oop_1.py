import math

class Point:
    def __init__(self, x,y,z) -> None:
        self.x=x
        self.y=y
        self.z=z

    def __getattribute__(self, __name: str) -> None:
        print('--__getattribute__')
        print(__name)

    def distanceTo(self, M):
        if type(M)==Point:
            return ((self.x-M.x)**2+(self.y-M.y)**2+(self.y-M.y)**2)**0.5
        else:
            return None

p = Point(0,0,0)

print(p.x)
