def read_contacts():
    contacts={}
    try:
        with open("contacts.txt", "r") as fh:
            contacts_list=fh.readlines()
            for contact in contacts_list:
                splitted_contact=contact.split()
                contacts[splitted_contact[0].rstrip(':')]=splitted_contact[1].rstrip('\n')
    except FileNotFoundError:
        pass
    except:
        print("There was an error while reading contacts.txt file") 

    return contacts