def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            user_input=input(f"There is already contact with the name {name}. Would you like to update it? yes/no ==> ")
            if user_input=="yes":
                contacts[name] = phone
                return f"Contact {name} was updated."
            elif user_input=="no":
                return "Aborted"
            else:
                return "Invalid command."
        else:
            contacts[name] = phone
            return f"Contact {name} was added."
    except ValueError:
        return "Please provide two arguments: name and phone"