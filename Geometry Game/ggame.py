from math import sqrt
from random import randint


class Point:   
    
    def __init__(self, x:int, y:int):
        '''
        Defining what would happen when we instantiate the class
        '''
        self._x = x
        self._y = y   

    def point_falls_in_rect(self, rect):
        if rect._lower_left._x < self._x < rect._upper_right._x and rect._lower_left._y < self._y < rect._upper_right._y:
            return True
        else:
            return False

    def distance(self, point):
        delta_x = self._x - point._x
        delta_y = self._y - point._y
        distance = delta_x**2 + delta_y**2
        return sqrt(distance)

    def __str__(self):
        # Modifying what happens when we print Point object
        return f'x-coordinate is {self._x}\ny-coordinate is {self._y}'


class Rectangle:
    
    def __init__(self, lower_left:Point, upper_right:Point):
        if type(lower_left) != Point or type(upper_right) != Point:
            lower_left = Point(lower_left[0], lower_left[1])
            upper_right = Point(upper_right[0], upper_right[1])
        self._lower_left = lower_left
        self._upper_right = upper_right

    def side_lengths(self):
        upper_left = Point(self._lower_left._x, self._upper_right._y)
        length1 = upper_left.distance(self._lower_left)
        length2 = upper_left.distance(self._upper_right)
        return (length1, length2)

    def area(self):
        sides = self.side_lengths()
        length = sides[0]
        width = sides[1]
        return length * width

    def __str__(self):
        return f'Rectangle Coordinates are\nLower Left : ({self._lower_left._x},{self._lower_left._y}) and\nUpper Right : ({self._upper_right._x},{self._upper_right._y})'


def random_rect(initial_lower:int = 0, difference:int = 9):
    initial_upper = initial_lower + difference + 1
    lower_left = Point(randint(initial_lower, initial_lower+difference),randint(initial_lower, initial_lower+difference))
    upper_right = Point(randint(initial_upper, initial_upper + difference), randint(initial_upper, initial_upper + difference))
    return Rectangle(lower_left, upper_right)

if __name__ == '__main__':
    rect1 = random_rect()
    print(rect1)
    
    user_point = Point(int(input("Guess X:")), int(input("Guess Y:")))
    print(f'Your point was inside the  rectangle : {user_point.point_falls_in_rect(rect1)}')
    
    consent = input("Do you want to play futher(y/n):")
    if consent == 'y' or consent == 'Y':
        guessed_area = int(input("Guess the area of rectangle:"))
        if guessed_area == rect1.area():
            print("Congo!! You gussed correct area!")
        else:
            print(f"Good luck for next time.\nWell correct area is {rect1.area()}")

    print("Ok thanks!!")
    