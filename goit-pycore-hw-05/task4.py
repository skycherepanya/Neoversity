# Додаємо декоритор для оброблення помилок.
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError: 
            func_name = func.__name__    
            if func_name in ["add_contact", "change_contact"]:
                return "Give me name and phone please."
            elif func_name == "show_phone":
                return "Enter user name."
            else:
                return "Index error: Not enough arguments provided."
    return inner


def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    if not contacts:
        return "No contacts saved."


    output = ""
    for name, phone in contacts.items():
        output += f"{name}: {phone}\n"
    
    return output.strip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break 
        
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))
        
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()