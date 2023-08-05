from main_menu_options import MAIN_MENU_OPTIONS


def phone_call_sum_price(price: float, call_history1) -> float:
    sum_call_price = price * len(call_history1)
    print(sum_call_price)
    return sum_call_price


def print_user_options():

    for i, option in enumerate(MAIN_MENU_OPTIONS, start=1):
        print(f"#{i} {option}")
