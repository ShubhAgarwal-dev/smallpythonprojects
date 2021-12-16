from main import *


def canvas_prompt() -> Canvas:
    width = int(input('Enter the canvas width(in px)?:'))
    height = int(input('Enter the canvas height(in px)?:'))
    color = color_prompt('canvas')
    image_path = input('What to name the image:?')
    canvas = Canvas(width, height, color, image_path)
    return canvas


def color_prompt(object_class: str = 'Object') -> list:
    red = abs(
        int(
            input(
                f'Please enter the amount of red you want in your {object_class}?\nPlease tell out of 255:'
            )))
    blue = abs(
        int(
            input(
                f'Please enter the amount of blue you want in your {object_class}?\nPlease tell out of 255:'
            )))
    green = abs(
        int(
            input(
                f'Please enter the amount of green you want in your {object_class}?\nPlease tell out of 255:'
            )))
    color = [red, green, blue]
    return color


def square_prompt(canvas: Canvas) -> Square:
    x_coordinate = abs(
        int(input('What is the upper-left x-coordinate of square: ')))
    y_coordinate = abs(
        int(input('What is the upper-left y-coordinate of square: ')))
    side = abs(int(input('Length of side of square is: ')))
    while True:
        if y_coordinate + side > canvas._height or x_coordinate + side > canvas._width:
            print('Please shorten the side so that it can fit in the canvas!')
            side = abs(int(input('Length of side of square is: ')))
        else:
            break
    color = color_prompt('square')
    square = Square(x_coordinate, y_coordinate, side, color)
    return square


def rectangle_prompt(canvas: Canvas) -> Rectangle:
    x_coordinate = abs(
        int(input('What is the upper-left x-coordinate of rectangle: ')))
    y_coordinate = abs(
        int(input('What is the upper-left y-coordinate of rectangle: ')))
    width = abs(int(input('Width of rectangle is: ')))

    while True:
        if x_coordinate + width > canvas._width:
            print(
                'Please shorten the rectangle width so that it can fit in the canvas!'
            )
            width = abs(int(input('Width of rectangle is: ')))
        else:
            break

    height = abs(int(input('Width of rectangle is: ')))
    while True:
        if y_coordinate + height > canvas._height:
            print(
                'Please shorten the rectangle height so that it can fit in the canvas!'
            )
            height = abs(int(input('Width of rectangle is: ')))
        else:
            break
    color = color_prompt('rectangle')
    return Rectangle(x_coordinate, y_coordinate, width, height, color)


def proceed_prompt():
    pass


if __name__ == '__main__':
    canvas = canvas_prompt()
