def name_data():
    name = input('Введите ваше имя: ')
    print('Красивое имя')
    return name

def surname_data():
    surname = input('Введите вашу фамилию: ')
    return surname

def phone_data():
    phone = input('Введите ваш телефон: ')
    return phone

def address_data():
    address = input('Введите ваш адрес: ')
    return address

class Contact:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.phone_number}"

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, first_name, last_name, phone_number):
        new_contact = Contact(first_name, last_name, phone_number)
        self.contacts.append(new_contact)
        print(f"Контакт {first_name} {last_name} добавлен.")

    def find_contact(self, name):
        results = []
        for contact in self.contacts:
            if name.lower() in contact.first_name.lower() or name.lower() in contact.last_name.lower():
                results.append(contact)
        return results
    
    def update_contact(self, name, new_first_name=None, new_last_name=None, new_phone_number=None):
        results = self.find_contact(name)
        if not results:
            print(f"Контакт с именем {name} не найден.")
            return
         
        for contact in results:
            if new_first_name:
                contact.first_name = new_first_name
            if new_last_name:
                contact.last_name = new_last_name
            if new_phone_number:
                contact.phone_number = new_phone_number
            print(f"Контакт {contact} обновлен.")

    def delete_contact(self, name):
        results = self.find_contact(name)
        if not results:
            print(f"Контакт с именем {name} не найден.")
            return

        for contact in results:
            self.contacts.remove(contact)
            print(f"Контакт {contact} удален.")

    def display_contacts(self):
        if not self.contacts:
            print("Телефонный справочник пуст.")
        else:
            for contact in self.contacts:
                print(contact)

def main():
    phonebook = PhoneBook()
    
    while True:
        print("\nТелефонный справочник")
        print("1. Добавить контакт")
        print("2. Найти контакт")
        print("3. Изменить контакт")
        print("4. Удалить контакт")
        print("5. Показать все контакты")
        print("6. Выйти из приложения")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            first_name = name_data()
            last_name = surname_data()
            phone_number = phone_data()
            phonebook.add_contact(first_name, last_name, phone_number)
        
        elif choice == '2':
            name = input("Введите имя или фамилию для поиска: ")
            found_contacts = phonebook.find_contact(name)
            if found_contacts:
                for contact in found_contacts:
                    print(contact)
            else:
                print("Контакт не найден.")
        
        elif choice == '3':
            name = input("Введите имя или фамилию контакта для изменения: ")
            new_first_name = input("Введите новое имя")
            new_last_name = input("Введите новую фамилию")
            new_phone_number = input("Введите новый номер телефона")
            phonebook.update_contact(name, new_first_name if new_first_name else None, new_last_name if new_last_name else None, new_phone_number if new_phone_number else None)
        
        elif choice == '4':
            name = input("Введите имя или фамилию контакта для удаления: ")
            phonebook.delete_contact(name)
        
        elif choice == '5':
            phonebook.display_contacts()
        
        elif choice == '6':
            print("До свидания!")
            break
        
        else:
            print("Неправильно выбрана команда. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
