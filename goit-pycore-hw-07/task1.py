from collections import UserDict
from datetime import datetime, date, timedelta


class Field:
    
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)
    

class Name(Field):
    
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value) 


class Birthday(Field):

    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
            date_object = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(date_object)

        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        

class Record:
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def add_phone(self, phone_number):
        new_phone = Phone(phone_number)
        self.phones.append(new_phone)


    def edit_phone(self, phone_number, new_phone):
        phone_to_edit = self.find_phone(phone_number)
        if not phone_to_edit:
            raise ValueError("Old phone not found.")
        Phone(new_phone)
        phone_to_edit.value = new_phone


    def delete_phone(self, phone_number):
        phone_to_delete = self.find_phone(phone_number)
        if not phone_to_delete:
            raise ValueError("Phone not found.")
        self.phones.remove(phone_to_delete)


    def find_phone(self, phone_number):
        for looking_for in self.phones:
            if looking_for.value == phone_number:
                return looking_for
              
    
    def add_birthday(self, birthday):
        new_birthday = Birthday(birthday)
        self.birthday = new_birthday


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    
    def add_record(self, record):
        key = record.name.value
        self.data[key] = record


    def find(self, name):
        return self.data.get(name)
    

    def delete(self, name):
        self.data.pop(name, None)
    

    def get_upcoming_birthdays(self):
        today = date.today()
        period = today + timedelta(days = 7) 
        result = []
    
        for record in self.data.values():
            if not record.birthday:
                continue

            birthday = record.birthday.value.date()
            this_year = birthday.replace(year=today.year)
           
            if this_year < today:
                this_year = this_year.replace(year=today.year + 1)

            if today <= this_year <= period:
                
                if this_year.weekday() == 5:
                    this_year = this_year + timedelta(days=2)
                elif this_year.weekday() == 6: #
                    this_year = this_year + timedelta(days=1)

                result.append({
                    "name": record.name.value,
                    "congratulation_date": this_year.strftime("%d.%m.%Y")
                })
        
        return result



def input_error(func):

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except ValueError as e:
        
            if "10 digits" in str(e) or "DD.MM.YYYY" in str(e):
                return f"Format error: {e}"

            else:
                return "Wrong arguments quantity."
        
        except IndexError:
           
            return "Not enough agruments."
        
        except AttributeError:
            
            return "Contact not found."

        except KeyError:

            return "Contact not found(KeyError)."

    return inner


def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    
    if record:
        record.edit_phone(old_phone, new_phone)
        return f"Phone for {name} changed."
    else:
        return f"Contact {name} not found."
    

@input_error
def show_phone(args, book: AddressBook):
    if not args:
        return "Enter name."
        
    name = args[0]
    record = book.find(name)
    
    if record:
        return str(record) 
    else:
        return f"Contact {name} not found."


@input_error
def show_all(args, book: AddressBook):
    if not book.data:
        return "Adress book empty."  
    
    output = "All contacts:\n"

    for record in book.data.values():
        output += f"{str(record)}\n"
        
    return output.strip()


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        return "Enter name and date of birth (DD.MM.YYYY)."
    
    name, birthday_date = args
    record = book.find(name)
    
    if record:
        record.add_birthday(birthday_date)
        return f"Birthday for {name} added."
    else:
        return f"Contact {name} not found."
    

@input_error
def show_birthday(args, book: AddressBook):
    if not args:
        return "Enter name."
        
    name = args[0]
    record = book.find(name)
    
    if record:
        if record.birthday:
            return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"
        else:
            return f"There is no bitrhday for {name}."
    else:
        return f"Contact {name} not found."


@input_error
def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    
    if not upcoming:
        return "There is no upcoming birthdays."
        
    output = "Upcoming birthdays:\n"
    for item in upcoming:
        output += f"  {item['name']}: {item['congratulation_date']}\n"
        
    return output.strip()


def main():
    book = AddressBook()
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
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()