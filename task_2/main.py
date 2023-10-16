from parse_input import parse_input
from utils import read_contacts, show_command_list, close_assistant


def main():
    contacts = read_contacts()
    if not contacts:
        print(show_command_list())

    while True:
        user_input = input("---> Enter a command: >>> ")
        command, args = parse_input(user_input)

        print(command(*args, contacts=contacts))
        
        if command == close_assistant:
            break
        
        # if command in CONTACT_COMMANDS:
        #     print(CONTACT_COMMANDS[command](args, contacts))

        # elif command == "hello":
        #     print(greet_user())

        # elif command == "help":
        #     print(show_command_list())

        # elif command == "all":
        #     print(show_all_contacts(contacts))

        # elif command in close_commands:
        #     print(close_assistant(contacts))
        #     break

        # else:
        #     print(INVALID_COMMAND)


if __name__ == "__main__":
    main()
