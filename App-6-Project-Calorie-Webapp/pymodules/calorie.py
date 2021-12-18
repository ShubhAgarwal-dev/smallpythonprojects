# type: ignore
# pyright: reportMissingModuleSource=false
from pymodules.temperature import Temperature


class Calorie():
    '''
    To calculate the optimal amount of
    calorie to take by a person
    '''

    def __init__(self, weight: float, height: float, age: int,
                 temperature: int) -> None:
        self._weight = weight  # in kg
        self._height = height  # in cm
        self._age = age  # in years
        self._temperature = temperature  # in celsius

    def calculate(self):
        result = 10 * self._weight + 6.5 * self._height + 5 - self._temperature * 10
        return result


if __name__ == '__main__':
    temp = Temperature(city='Shahjahanpur', country='India')
    calorie = Calorie(weight=70, height=173, age=32, temperature=temp.get())
    print(calorie.calculate())
