from constants import EMPTY_PHONEBOOK


def read_contacts():
    contacts = {}
    try:
        with open("task_2/contacts.txt", "r") as fh:
            contacts_list = fh.readlines()
            for contact in contacts_list:
                splitted_contact = contact.split()
                contacts[splitted_contact[0].rstrip(":")] = splitted_contact[1].rstrip(
                    "\n"
                )
    except FileNotFoundError:
        print(EMPTY_PHONEBOOK)
    except:
        print("There was an error while reading the phonebook")

    return contacts
