class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('This is to move')

    def draw(self):
        print('This is to draw')


point = Point(10, 20)
point.y = 40
print(point.x, point.y)
print(point.draw())
