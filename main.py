from utils import *

close_commands = ["close", "exit", "bye", "stop"]

def main():
    contacts=read_contacts()

    while True:
        user_input = input("---> Enter a command: ")
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

        else:
            print("Invalid command. Type 'help' to get the list of valid commands. ")

if __name__=="__main__":
    main()