def change_contact(args, contacts):
    try:
        name, phone = args
        if name not in contacts:
            user_input=input(f"There is no contact with the name {name}. Would you like to add? yes/no ==> ")
            if user_input=="yes":
                contacts[name] = phone
                return f"Contact {name} was added."
            elif user_input=="no":
                return "Aborted"
            else:
                return "Invalid command."
        else:
            contacts[name] = phone
            return f"Contact {name} was updated."
    except ValueError:
        return "Please provide two arguments: name and phone"