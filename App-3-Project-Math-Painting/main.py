from typing import Iterable
import numpy as np
from PIL import Image


class Canvas:
    '''
    To make and handle the canvas
    '''

    def __init__(self, width: int, height: int, color: Iterable,
                 image_path) -> None:
        self._width = width
        self._height = height
        self._color = color
        self.image_path = image_path

    def canvas_data(self):
        '''
        To tell the current state of canvas
        '''
        img = Image.open(self.image_path)
        canvas_data = np.asarray(img)
        img.close()
        return canvas_data

    def make(self):
        canvas_data = np.zeros((self._height, self._width, 3), dtype=np.uint8)
        canvas_data[:] = list(self._color)
        canvas_img = Image.fromarray(canvas_data, mode='RGB')
        canvas_img.save(self.image_path)


class Square:
    '''
    To make and draw square on the canvas
    '''

    def __init__(self, x: int, y: int, side: int, color: Iterable) -> None:
        self._x = x
        self._y = y
        self._side = side
        self._color = color

    def draw(self, canvas: Canvas):
        '''
        Draw square on the canvas
        '''
        canvas_data = canvas.canvas_data()
        canvas_data[self._y:self._y + self._side,
                    self._x:self._x + self._side] = list(self._color)
        canvas_img = Image.fromarray(canvas_data, mode='RGB')
        canvas_img.save(canvas.image_path)


class Rectangle:
    '''
    To deal with rectangle shape
    '''

    def __init__(self, x: int, y: int, width: int, height: int,
                 color: Iterable) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color

    def draw(self, canvas: Canvas):
        '''
        To draw rectangle on the canvas
        '''
        canvas_data = canvas.canvas_data()
        canvas_data[self._y:self._y + self._height,
                    self._x:self._x + self._width] = list(self._color)
        canvas_img = Image.fromarray(canvas_data, mode='RGB')
        canvas_img.save(canvas.image_path)


if __name__ == '__main__':
    canvas = Canvas(1000, 1500, [255, 255, 0], 'canvas2.png')
    canvas.make()
    square = Square(100, 150, 200, [100, 56, 250])
    square.draw(canvas)
    rect = Rectangle(200, 400, 100, 300, [100, 230, 50])
    rect.draw(canvas)
