from utils import (
    add_contact,
    change_contact,
    show_all_contacts,
    delete_contact,
    show_phone_number,
    parse_input,
    greet_user,
    read_contacts,
    show_command_list,
    close_assistant,
)
from constants import INVALID_COMMAND

close_commands = ["close", "exit", "stop"]


def main():
    contacts = read_contacts()
    if not contacts:
        print(show_command_list())

    while True:
        user_input = input("---> Enter a command: >>> ")
        command, *args = parse_input(user_input)

        CONTACT_COMMANDS = {
            "add": add_contact,
            "change": change_contact,
            "phone": show_phone_number,
            "delete": delete_contact,
        }
        if command in CONTACT_COMMANDS:
            print(CONTACT_COMMANDS[command](args, contacts))

        elif command == "hello":
            print(greet_user())

        elif command == "help":
            print(show_command_list())

        elif command == "all":
            print(show_all_contacts(contacts))

        elif command in close_commands:
            print(close_assistant(contacts))
            break

        else:
            print(INVALID_COMMAND)


if __name__ == "__main__":
    main()
