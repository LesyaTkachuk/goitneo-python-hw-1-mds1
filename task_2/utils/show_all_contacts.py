from constants import EMPTY_PHONEBOOK


def show_all_contacts(contacts):
    if not len(contacts):
        return EMPTY_PHONEBOOK
    contacts_list = list()
    for name, phone in contacts.items():
        contacts_list.append("{:<10}:  {}".format(name, phone))
    contacts_string = "\n".join(contacts_list)
    return f"{'*'*15}\n{contacts_string}\n{'*'*15}"
