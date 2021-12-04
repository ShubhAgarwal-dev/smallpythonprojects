# Code from main.py is being reorganized


class Bill():
    '''
    Object that contain data about bill.
    Such as total amount, period of bill, etc.
    '''

    def __init__(self, amount: int, period: str) -> None:
        self._amount = amount
        self._period = period


class Flatmate():
    '''
    Object for flatmate(or anyone for that matter) that live with you 
    and pays share of bill.
    '''

    def __init__(self, name: str, days_in_house: int = 30) -> None:
        self._name = name
        self._days = days_in_house

    def pays(self, bill: Bill, *flatmates):
        sum = self._days
        for i in flatmates:
            sum += i._days
        weight = self._days / sum
        return weight * bill._amount
