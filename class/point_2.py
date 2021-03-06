class Point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def set_point(self, x, y):
        self.x=x
        self.y=y

    def get_point(self):
        return self.x, self.y

    def __str__(self):
        return ('({}, {})'.format(self.x, self.y))

    def __add__(self, n):
        x=self.x+n
        y=self.y+n
        return Point(x, y)

    def __radd__(self, n):
        x=self.x+n
        y=self.y+n
        return Point(x, y)

if __name__=="__main__":
    p1=Point(2, 2)
    p2=p1+3
    #p2=3+p1
    print(p2)