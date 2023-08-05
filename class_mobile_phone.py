from class_phone_battery import PhoneBattery
from class_phone_screen import PhoneScreen
from class_call import Call
from typing import List


# def phone_call_sum_price(price: int, call_history1: int) -> int:
#     sum_call_price = price * len(call_history1)
#     print(sum_call_price)
#     return sum_call_price


class MobilePhone:

    @staticmethod
    def nokia_n95():
        return MobilePhone('Nokia', 'N95', 2000, 'Tiho', None, None)

    # def nokia_model(self):
    #     print(self.nokiaN95)

    def __init__(self,
                 model='',
                 manufacturer='',
                 price=0,
                 owner='',
                 battery: PhoneBattery = None,
                 screen: PhoneScreen = None
                 ):
        self._model = model
        self._manufacturer = manufacturer
        self._price = price
        self._owner = owner
        self._battery = battery
        self._screen = screen
        self._call_history = []

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model}"

    def call(self, to):
        print(f"Calling {to}")
        self._call_history.append(Call('me', to, 'Today', 'One hour ago', 20))

    @property
    def call_history(self) -> List[Call]:
        return self._call_history

    @property
    def model(self):
        return self._model

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def price(self):
        return self._price

    @property
    def battery(self):
        return self._battery

    @property
    def screen(self):
        return self._screen

    def add_new_call(self):
        # call_h = []
        # call_list1 = []
        print('Add New Phone Call')
        name_person_call = input('Enter the name of the person who is calling\n')
        name_recipient_call = input('Enter the name of the person you are calling\n')
        date_call = input('Enter the date call\n')
        start_time_call = input('Enter the time call\n')
        duration_call = int(input('Enter the call duration\n'))
        call_h = [name_person_call, name_recipient_call, date_call, start_time_call, duration_call]
        # print(call_h)
        self._call_history.append(call_h)
        # call_list1.append(call_h)
        print(self.call_history)
        # print(call_list1)
        print(len(self.call_history))
        return self.call_history
        # return call_list1

    def delete_call(self):
        print(self.call_history)
        self.call_history.pop()
        return self.call_history

