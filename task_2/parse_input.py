from utils import (
    add_contact,
    change_contact,
    show_all_contacts,
    delete_contact,
    show_phone_number,
    greet_user,
    show_command_list,
    close_assistant,
    unknown_command
)

CONTACT_COMMANDS = {
            "add": add_contact,
            "change": change_contact,
            "phone": show_phone_number,
            "delete": delete_contact,
            "hello": greet_user,
            "help": show_command_list,
            "all": show_all_contacts,
            ("close", "exit", "stop"): close_assistant 
        }


def parse_input(user_input):
        # cmd_kw, *args = user_input.split()
        for kw, command in CONTACT_COMMANDS.items():
            if user_input.startswith(kw):
                return command, user_input.split()[1:]
        return unknown_command, []