def show_command_list():
    return """
    *****************************
    add <name> <phone>      --> to add a contact with the provided phone number to the phonebook
    change <name> <phone>   --> to change the existing contact's phone number
    phone <name>            --> to display the existing contact's phone number
    delete <name>           --> to delete provided contact with a phone number from the phonebook
    all                     --> to display the whole phone book
    exit | stop | close     --> to exit and store contacts
    ******************************
    """
