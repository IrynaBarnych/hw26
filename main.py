# Завдання 5
# Реалізуйте клас «Вебсайт». Збережіть у класі:
# назву вебсайту, адресу та опис вебсайту.
# Реалізуйте конструктор та методи класу для введення-виведення даних, а також
# для інших операцій. Використовуйте механізм перевантаження методів.

class Website:
    def __init__(self, name, adres, describe):
        self.name = name
        self.adres = adres
        self.describe = describe

    def get_name(self):
        return self.name

    def get_adres(self):
        return self.adres

    def get_describe(self):
        return self.describe

website1 = Website("Вікіпедія", "https://uk.wikipedia.org", "Вікіпе́дія — загальнодоступна вільна багатомовна онлайн-енциклопедія")
website2 = Website("YouTube", "https://www.youtube.com/", "YouTube — популярний відеохостинг, що надає послуги розміщення відеоматеріалів")

print(f"Назва вебсайту: {website1.get_name()}")
print(f"Адреса вебсайту: {website1.get_adres()}")
print(f"Опис вебсайту: {website1.get_describe()}")

print(f"Назва вебсайту: {website2.get_name()}")
print(f"Адреса вебсайту: {website2.get_adres()}")
print(f"Опис вебсайту: {website2.get_describe()}")



