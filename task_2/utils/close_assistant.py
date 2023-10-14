def close_assistant(contacts):
    if contacts:
        contact_list = list()
        for key, value in contacts.items():
            contact_list.append(f"{key}: {value}\n")
        with open("task_2/contacts.txt", "w") as fh:
            fh.writelines(contact_list)

    return "Good bye!"
