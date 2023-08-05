
from class_mobile_phone import MobilePhone
from ui import phone_call_sum_price, print_user_options

print_user_options()
phone = MobilePhone()
call_list = []
call_list_res = []

try:
    select = int(input('Select your choice\n'))
    while select != 3:
        if select == 1:
            call_list = phone.add_new_call()
            call_list_res = call_list
            answer = input('Do you want to add another call?\n')
            if answer == 'Yes':
                select = 1
            elif answer == 'No':
                select = int(input('Select your choice\n'))
                # while not select.isdigit() or (select.isdigit() and 3 < int(select) < 1):
                #     select = input('Select your choice\n')
        elif select == 2:
            choice = 'Delete Phone Call'
            call_list = phone.delete_call()
            call_list_res = call_list
            print(call_list_res)
            answer2 = input('Do you want to delete another call?\n')
            if answer2 == 'Yes':
                call_list_res.pop()
                select = 2
            else:
                select = int(input('Select your choice\n'))
                # while not select.isdigit() or (select.isdigit() and 3 < int(select) < 1):
                #     select = input('Select your choice\n')
except ValueError:
    print('Not a number')
call_price = float(input('Enter the call price\n'))
print(phone_call_sum_price(call_price, call_list_res))
exit()
