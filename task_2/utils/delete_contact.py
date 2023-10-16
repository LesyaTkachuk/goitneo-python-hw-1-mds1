from constants import YES_CHOICE, NO_CHOICE, YES_NO_CHOICE, ABORTED, INVALID_COMMAND


def delete_contact(*args, contacts):
    try:
        name = args[0]
        user_input = input(
            f"Do you really want to delete {name} from contacts?{YES_NO_CHOICE}"
        )
        user_input = user_input.strip().lower()

        if user_input == YES_CHOICE:
            if name in contacts:
                contacts.pop(name)
                return f"Contact {name} was deleted."
            else:
                return f"Contact with the name {name} doesn't exists in contacts"

        elif user_input == NO_CHOICE:
            return ABORTED
        else:
            return INVALID_COMMAND

    except IndexError:
        return "Please provide contact's name to delete"
