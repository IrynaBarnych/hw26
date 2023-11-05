# Завдання 5
# Реалізуйте клас «Вебсайт». Збережіть у класі:
# назву вебсайту, адресу та опис вебсайту.
# Реалізуйте конструктор та методи класу для введення-виведення даних, а також
# для інших операцій. Використовуйте механізм перевантаження методів.

class Website:
    def __init__(self, name, adres, describe, watch):
        self.name = name
        self.adres = adres
        self.describe = describe
        self.watch = watch

    def get_name(self):
        return self.name

    def get_adres(self):
        return self.adres

    def get_describe(self):
        return self.describe
    def get_watch(self):
        return self.watch

    def __sub__(self, other):
        return self.watch - other.watch

website1 = Website("Вікіпедія", "https://uk.wikipedia.org", "Вікіпе́дія — загальнодоступна вільна багатомовна онлайн-енциклопедія", 1000000)
website2 = Website("YouTube", "https://www.youtube.com/", "YouTube — популярний відеохостинг, що надає послуги розміщення відеоматеріалів", 1000000000)

print(f"Назва вебсайту: {website1.get_name()}")
print(f"Адреса вебсайту: {website1.get_adres()}")
print(f"Опис вебсайту: {website1.get_describe()}")
print(f"Кількість перегляду за рік: {website1.get_watch()}")

print(f"Назва вебсайту: {website2.get_name()}")
print(f"Адреса вебсайту: {website2.get_adres()}")
print(f"Опис вебсайту: {website2.get_describe()}")
print(f"Кількість перегляду за рік: {website2.get_watch()}")

if website1.get_watch() > website2.get_watch():
    print("Вікіпедія користується більшим попитом.")
else:
    print("YouTube користується більшим попитом.")

difference = abs(website1 - website2)
print(f"Різниця в переглядах: {difference}")

