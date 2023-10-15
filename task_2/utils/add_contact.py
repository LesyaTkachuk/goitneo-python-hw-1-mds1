from constants import YES_CHOICE, NO_CHOICE, YES_NO_CHOICE, ABORTED, INVALID_COMMAND


def add_contact(*args, contacts):
    try:
        name, phone = args
        if name in contacts:
            user_input = input(
                f"Contact {name} already exists. Would you like to update it?{YES_NO_CHOICE}"
            )
            user_input = user_input.strip().lower()

            if user_input == YES_CHOICE:
                contacts[name] = phone
                return f"Contact {name} was updated."
            elif user_input == NO_CHOICE:
                return ABORTED
            else:
                return INVALID_COMMAND
        else:
            contacts[name] = phone
            return f"Contact {name} was added."
    except ValueError:
        return "Please provide two arguments: name and phone"
