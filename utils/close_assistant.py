def close_assistant(contacts):
    contact_list=list()
    for key,value in contacts.items():
        contact_list.append(f'{key}: {value}\n')
    with open("contacts.txt", 'w') as fh:
        fh.writelines(contact_list)