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

# Створення екземпляра класу
Country1 = Country("Україна", "Європа", "44 млн.", "+380",
               "Київ", "Харків, Херсон, Миколаїв, Одеса")

# Виведення інформації про Країну
print(f"Назва країни: {Country1.get_name()}")
print(f"Назва континенту: {Country1.get_continent()}")
print(f"Кількість жителів країни: {Country1.get_population()}")
print(f"Телефонний код країни: {Country1.get_country_code()}")
print(f"Назву столиці: {Country1.get_capital()}")
print(f"Назву міст країни: {Country1.get_cities()}")


