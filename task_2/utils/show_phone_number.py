def show_phone_number(*args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return f"{name}'s phone number is {contacts[name]}"
        else:
            return f"Contact with the name {name} was not found"
    except IndexError:
        return "Please provide name of the user"
