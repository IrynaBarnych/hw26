# Завдання 3
# До вже реалізованого класу «Країна» додайте конструктор та необхідні перевантажені методи.

class Country:
    def __init__(self, name, continent, country_code, population, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.country_code = country_code
        self.capital = capital
        self.cities = cities

    def get_name(self):
        return self.name

    def get_continent(self):
        return self.continent

    def get_population(self):
        return self.population

    def get_country_code(self):
        return self.country_code

    def get_capital(self):
        return self.capital

    def get_cities(self):
        return self.cities

    def compare_continent(self, other_country):
        return self.continent == other_country.get_continent()

    def __sub__(self, other):
        return self.population - other.population

# Створення екземпляра класу
Country1 = Country("Україна", "Європа", "+38", 44,
               "Київ", "Харків, Херсон, Миколаїв, Одеса")

Country2 = Country("Австралія", "Океанія", "+61", 25,
                   "Сідней", "Сідней, Мельбурн, Брісбен, Перт")


# Виведення інформації про Країну1
print(f"Назва країни: {Country1.get_name()}")
print(f"Назва континенту: {Country1.get_continent()}")
print(f"Кількість жителів країни: {Country1.get_population()}")
print(f"Телефонний код країни: {Country1.get_country_code()}")
print(f"Назву столиці: {Country1.get_capital()}")
print(f"Назву міст країни: {Country1.get_cities()}")

# Виведення інформації про Країну2
print(f"Назва країни: {Country2.get_name()}")
print(f"Назва континенту: {Country2.get_continent()}")
print(f"Кількість жителів країни: {Country2.get_population()}")
print(f"Телефонний код країни: {Country2.get_country_code()}")
print(f"Назву столиці: {Country2.get_capital()}")
print(f"Назву міст країни: {Country2.get_cities()}")

if Country1.compare_continent(Country2):
    print("Ці країни знаходяться на одному континенті.")
else:
    print("Ці країни знаходяться на різних континентах.")

difference = abs(Country1 - Country2)
print(f"Різниця в населені: {difference} млн.")
