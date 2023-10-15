from constants import YES_CHOICE, NO_CHOICE, ABORTED, INVALID_COMMAND, YES_NO_CHOICE


def change_contact(*args, contacts):
    try:
        name, phone = args
        if name not in contacts:
            user_input = input(
                f"There is no contact with the name {name}. Would you like to add?{YES_NO_CHOICE}"
            )
            user_input = user_input.strip().lower()

            if user_input == YES_CHOICE:
                contacts[name] = phone
                return f"Contact {name} was added."
            elif user_input == NO_CHOICE:
                return ABORTED
            else:
                return INVALID_COMMAND
        else:
            contacts[name] = phone
            return f"Contact {name} was updated."
    except ValueError:
        return "Please provide two arguments: name and phone"
