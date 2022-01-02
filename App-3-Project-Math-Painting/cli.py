from main import *
from os import path as ospath
import sys


def canvas_prompt() -> Canvas:
    '''
    It would make your canvas from series of terminal inputs
    '''
    width = int(input('Enter the canvas width(in px): '))
    height = int(input('Enter the canvas height(in px): '))
    color = color_prompt('canvas')
    image_path = input('What to name the image: ')
    if ospath.splitext(image_path)[1] != '.png':
        image_path += '.png'
    canvas = Canvas(width, height, color, image_path)
    return canvas


def color_prompt(object_class: str = 'Object') -> list:
    '''
    To make colour for your shapes or canvas
    '''
    print('')
    red = abs(
        int(
            input(
                f'Please enter the amount of red you want in your {object_class}? Please tell out of 255: '
            )))
    green = abs(
        int(
            input(
                f'Please enter the amount of green you want in your {object_class}? Please tell out of 255: '
            )))
    blue = abs(
        int(
            input(
                f'Please enter the amount of blue you want in your {object_class}? Please tell out of 255: '
            )))
    print('')
    color = [red, green, blue]
    return color


def square_prompt(canvas: Canvas):
    '''
    To draw square in canvas
    from relatively user-friendly terminal inputs
    '''
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
    square.draw(canvas)


def rectangle_prompt(canvas: Canvas):
    '''
    To draw rectangle in canvas
    from relatively user-friendly terminal inputs
    '''
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

    height = abs(int(input('Height of rectangle is: ')))
    while True:
        if y_coordinate + height > canvas._height:
            print(
                'Please shorten the rectangle height so that it can fit in the canvas!'
            )
            height = abs(int(input('Width of rectangle is: ')))
        else:
            break
    color = color_prompt('rectangle')
    rect = Rectangle(x_coordinate, y_coordinate, width, height, color)
    rect.draw(canvas)


def proceed_prompt(canvas: Canvas):
    '''
    To proceed the cli for more shapes
    '''
    print('What do you want to do further?')
    while True:
        responce = input('Type s for square, r for rectangle or q to quit: ')
        if responce == 's' or responce == 'S':
            square_prompt(canvas)
            break
        elif responce == 'r' or responce == 'R':
            rectangle_prompt(canvas)
            break
        elif responce == 'q' or responce == 'Q':
            print('Are you sure')
            responce2 = input('Type q again to quit: ')
            if responce2 == 'q' or responce2 == 'Q':
                sys.exit()
            else:
                continue
        else:
            print('Please type correct responce!!')
            continue


if __name__ == '__main__':
    canvas = canvas_prompt()
    canvas.make()
    print('What would you like to draw on the canvas you made? ')
    while True:
        responce = input('Type s for square or r for rectangle: ')
        if responce == 's' or responce == 'S':
            square_prompt(canvas)
            break
        elif responce == 'r' or responce == 'R':
            rectangle_prompt(canvas)
            break
        else:
            print('Please type correct responce!!')
            continue
    while True:
        proceed_prompt(canvas)
