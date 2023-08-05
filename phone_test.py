import unittest
from class_mobile_phone import MobilePhone
from class_phone_screen import PhoneScreen
from class_phone_battery import PhoneBattery
from class_battery_type import BatteryType
from ui import phone_call_sum_price
# from class_call import Call
# from main import MobilePhone, PhoneBattery, PhoneScreen, BatteryType, Call


class PhoneTest(unittest.TestCase):
    def test_battery(self):
        battery = PhoneBattery('kljl', 160, 20)
        # screen: PhoneScreen = PhoneScreen(120, 200, 16_000_000)
        phone = MobilePhone('Nokia', '3310', 110, 'me', battery)
        self.assertEqual(phone.battery.model, 'kljl')
        self.assertEqual(phone.battery.idle_time, 160)
        self.assertEqual(phone.battery.hours_talk, 20)

    def test_screen(self):
        battery = PhoneBattery('kljl', 160, 20)
        screen: PhoneScreen = PhoneScreen(120, 200, 16_000_000)
        phones = [MobilePhone('Nokia', '3310', 110, 'me', battery, screen) for _ in range(5)]
        for phone in phones:
            self.assertEqual(phone.screen.colors, 16_000_000)
            self.assertEqual(phone.screen.width, 120)
            self.assertEqual(phone.screen.height, 200)

    def test_nokia_n95(self):
        phone = MobilePhone.nokia_n95()
        self.assertEqual(phone.model, 'Nokia')
        self.assertEqual(phone.manufacturer, 'N95')
        print(phone)

    def test_fail(self):
        battery = PhoneBattery('kljl', 160, 20, BatteryType.LI_ION)
        screen: PhoneScreen = PhoneScreen(120, 200, 16_000_000)
        phone = MobilePhone('Nokia', '3310', 110, 'me', battery, screen)
        self.assertEqual(phone.battery.type, BatteryType.LI_ION)
        print(phone.battery.type.value)
        print(phone.battery.type.name)

    def test_call_history(self):
        battery = PhoneBattery('kljl', 160, 20, BatteryType.LI_ION)
        screen: PhoneScreen = PhoneScreen(120, 200, 16_000_000)
        phone = MobilePhone('Nokia', '3310', 110, 'me', battery, screen)
        # self.assertEqual(len(phone.call_history), 0)
        phone.call('12345')
        # self.assertEqual(len(phone.call_history), 1)
        recent_call = phone.call_history[-1]
        print(recent_call)
        self.assertEqual(recent_call.caller, 'me')
        self.assertEqual(recent_call.duration_time, 20)
        self.assertEqual(recent_call.to, '12345')

    def test_gsm_call_history(self):
        battery = PhoneBattery('kljl', 160, 20, BatteryType.LI_ION)
        screen: PhoneScreen = PhoneScreen(120, 200, 16_000_000)
        phone = MobilePhone('Nokia', '3310', 110, 'me', battery, screen)
        phone.add_new_call()
        num_call = phone.add_new_call()
        len_call = len(num_call)
        self.assertEqual(len_call, 2)
        self.assertEqual(phone_call_sum_price(3, num_call), 6)
        print(num_call)
        # self.assertEqual(len(phone.delete_call()), 1)
        # self.assertEqual(len(phone.delete_call()), 0)
        self.assertEqual(num_call[0][4], 32)
        self.assertEqual(num_call[1][4], 23)
        if num_call[0][4] > num_call[1][4]:
            num_call.pop(0)
        else:
            num_call.pop(1)
        print(num_call)
        self.assertEqual(len(num_call), 1)
        self.assertEqual(len(phone.delete_call()), 0)
        # self.assertEqual(num_call[4], 4)


if __name__ == '__main__':
    unittest.main()
