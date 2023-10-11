from utils import *
from constants import INVALID_COMMAND

close_commands = ["close", "exit", "stop"]

def main():
    contacts=read_contacts()
    if not contacts:
        print(show_command_list())


    while True:
        user_input = input("---> Enter a command: >>> ")
        command, *args = parse_input(user_input)

        if command in close_commands:
            close_assistant(contacts)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            print(add_contact(args, contacts))

        elif command in ["change", "edit"]:
            print(change_contact(args, contacts))
        
        elif command == "phone":
            print(show_phone_number(args, contacts))

        elif command == "all":
            print(show_all_contacts(contacts))
        
        elif command == "help":
            print(show_command_list())
        
        elif command == "delete":
            print(delete_contact(args, contacts))

        else:
            print(INVALID_COMMAND)

if __name__=="__main__":
    main()