class Point:
    def move(self):
        print('This is to move')
    def draw(self):
        print('This is to draw')


point1 = Point()
point1.x = 10
point1.y = 20
point1.draw()

point2 = Point()
point2.x = 5
point2.move()
