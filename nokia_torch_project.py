def handle_phone_book():
    while True:
        print_phone_book_menu()
        user_input = int(input())

        if user_input == 1:
            print("Search Activated")
        elif user_input == 2:
            print("Service Nos Activate")
        elif user_input == 3:
            print("Add name Activated")
        elif user_input == 4:
            print("Erase Activated")
        elif user_input == 5:
            print("Edit Activated")
        elif user_input == 6:
            print("Assign tone Activated")
        elif user_input == 7:
            print("Send b'card is Activated")
        elif user_input == 8:
            handle_phone_book_option()
        elif user_input == 9:
            print("Speed dial activated")
        elif user_input == 10:
            print("Voice tag activated")
        elif user_input == 0:
            return
        else:
            print("Wrong input, try again!!")


def print_phone_book_menu():
    print("""
        Phone Book:
        1-> Search
        2-> Service Nos.
        3-> Add name
        4-> Erase
        5-> Edit
        6-> Assign tone
        7-> Send b'card
        8-> Option
        9-> Speed dials
        10-> Voice tags
        0-> Back to main menu
        """)


def handle_phone_book_option():
    print("""
        Option
        1-> Type of view
        2-> Memory Status
        """)
    user_input = int(input())
    if user_input == 1:
        print("Type of view Activated")
    elif user_input == 2:
        print("Memory Status Activated")
    else:
        print("Sorry wrong input, try again.")


def handle_call_register():
    while True:
        print_call_register_menu()
        call_register = int(input())

        if call_register == 1:
            print("Missed calls")
        elif call_register == 2:
            print("Received calls")
        elif call_register == 3:
            print("Dialled numbers")
        elif call_register == 4:
            print("Erase recent call list")
        elif call_register == 5:
            handle_show_call_duration()
        elif call_register == 6:
            handle_show_call_cost()
        elif call_register == 7:
            handle_call_cost_settings()
        elif call_register == 8:
            print("Prepaid credit")
        elif call_register == 0:
            return
        else:
            print("Wrong input, try again.")


def print_call_register_menu():
    print("""
        Call register:
        1-> Missed calls
        2-> Received calls
        3-> Dialled numbers
        4-> Erase recent call lists
        5-> Show call duration
        6-> Show call cost
        7-> Call cost settings
        8-> Prepaid credit
        0-> Back to main menu
        """)


def handle_show_call_duration():
    print("""
        Show call duration:
        1-> Last call duration
        2-> All call's duration
        3-> Received call's duration
        4-> Dialled calls duration
        5-> Clear timers
        0-> Back to call register menu
        """)

    show_call_duration = int(input())
    if show_call_duration == 1:
        print("Last call duration")
    elif show_call_duration == 2:
        print("All call's duration")
    elif show_call_duration == 3:
        print("Received call's duration")
    elif show_call_duration == 4:
        print("Dialled calls duration")
    elif show_call_duration == 5:
        print("Clear timers")
    elif show_call_duration == 0:

    else:
        print("Wrong input, try again.")


def handle_show_call_cost():

def handle_call_cost_settings():



def handle_tones():


def handle_settings():


def handle_clock():
    while True:
        print_clock_menu()
        clock = int(input())

        if clock == 0:
            break
        else:
            print("Wrong input, try again!!")


def print_clock_menu():
    print("""
            Clock:
            1-> Alarm clock
            2-> Clock setting
            3-> Date setting
            4-> Stopwatch
            5-> Countdown timer
            6-> Auto update of date and time
            0-> Back to Main Menu
            Select option:
            """)


def handle_messages():
    while True:
        print_messages_menu()
        user_input = int(input())

        if user_input == 7:
            handle_message_settings()
        elif user_input == 0:
            return
        else:
            print("Wrong input, try again!!")


def print_messages_menu():
    print("""
        Messages:
        1-> Inbox
        2-> Sent items
        3-> Drafts
        4-> Templates
        5-> Smileys
        6-> Message settings
        7-> Common
        0-> Back to main menu
        """)


def handle_message_settings():
    print("""
        Message setting
        1-> Set
        2-> Common

        Select option
        """)
    message = int(input())
    if message == 1:
        handle_set_message()
    elif message == 2:
        handle_common_message()
    elif message == 0:

    else:
        print("Wrong input, try again!!")


def handle_set_message():
    print("""
        Set1
        1-> Message Centre number
        2-> Message sent as
        3-> Message validity

        Select option:
        """)
    set_option = int(input())
    if set_option == 0:
        return  # Go back to the message settings menu
    else:
        print("Wrong entry, try again ")


def handle_common_message():
    print("""
        Common
        1-> Delivery report
        2-> Reply via same centre
        3-> Character Support

        Select Option
        """)
    common_option = int(input())
    if common_option == 0:
        return
    else:
        print("Wrong input, try again")


def print_main_menu():
    print("""
        Menu:
        1-> Phone book
        2-> Messages
        3-> Chart
        4-> Call Register
        5-> Tones
        6-> Settings
        7-> Call Divert
        8-> Games
        9-> Calculator
        10-> Reminders
        11-> Clock
        12-> Profiles
        13-> SIM services
        0-> Exit
        """)


def main():
    while True:
        print_main_menu()
        user_input = int
