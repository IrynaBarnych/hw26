# Завдання 1
# До вже реалізованого класу «Людина» додайте конструктор та необхідні перевантажені методи.

class People:
    def __init__(self, full_name, date_of_birth, contact_phone_number, city, country, home_address):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.contact_phone_number = contact_phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

    def get_full_name(self):
        return self.full_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_contact_phone_number(self):
        return self.contact_phone_number

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country

    def get_home_address(self):
        return self.home_address

# Створення екземпляра класу
person = People("Шевченко Т.Г.", "2010-03-09", "0661234567", "Київ",
               "Україна", "вул. Листопадна буд. 4")

# Виведення інформації про Людину
print(f"ПІБ: {person.get_full_name()}")
print(f"Дата народження: {person.get_date_of_birth()}")
print(f"Контактний телефон: {person.get_contact_phone_number()}")
print(f"Місто: {person.get_city()}")
print(f"Країна: {person.get_country()}")
print(f"Домашня адреса: {person.get_home_address()}")


