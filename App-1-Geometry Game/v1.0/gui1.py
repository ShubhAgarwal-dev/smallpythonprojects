import ggame
import turtle
from random import randint


class GuiPoint(ggame.Point):
    def draw(self, canvas: turtle.Turtle, size=5, color='blue'):
        canvas.penup()
        canvas.goto(self._x * 20, self._y * 20)
        canvas.pendown()
        canvas.dot(size, color)


class GuiRectangle(ggame.Rectangle):
    def draw(self, canvas: turtle.Turtle):
        # -> Going to certain coordinate
        canvas.penup()
        canvas.goto(self._lower_left._x * 20, self._upper_right._y * 20)
        turtle.mode("logo")

        canvas.pendown()
        length = self.side_lengths()[0] * 20
        width = self.side_lengths()[1] * 20
        canvas.forward(length)
        canvas.right(90)
        turtle.delay(20)
        canvas.forward(width)
        canvas.right(90)
        turtle.delay(20)
        canvas.forward(length)
        canvas.right(90)
        turtle.delay(20)
        canvas.forward(width)
        canvas.right(90)
        turtle.delay(20)


def random_gui_rect(initial_lower: int = 0, difference: int = 9):
    initial_upper = initial_lower + difference + 1
    lower_left = ggame.Point(
        randint(initial_lower, initial_lower + difference),
        randint(initial_lower, initial_lower + difference))
    upper_right = ggame.Point(
        randint(initial_upper, initial_upper + difference),
        randint(initial_upper, initial_upper + difference))
    return GuiRectangle(lower_left, upper_right)


if __name__ == '__main__':
    gui_rect1 = random_gui_rect()
    guipoint1 = GuiPoint(3, 7)
    my_turtle = turtle.Turtle()
    gui_rect1.draw(my_turtle)
    guipoint1.draw(my_turtle)

    turtle.hideturtle()
    turtle.done()
