# Завдання 2
# До вже реалізованого класу «Місто» додайте конструктор та необхідні перевантажені методи.


class City:
    def __init__(self, city_name, region, country_name, population, postal_code, city_code, distance):
        self.city_name = city_name
        self.region = region
        self.country_name = country_name
        self.population = population
        self.postal_code = postal_code
        self.city_code = city_code
        self.distance = distance

    def get_city_name(self):
        return self.city_name

    def get_region(self):
        return self.region

    def get_country_name(self):
        return self.country_name
    def get_population(self):
        return self.population

    def get_postal_code(self):
        return self.postal_code

    def get_city_code(self):
        return self.city_code

    def get_city_code(self):
        return self.distance

# Створення екземпляра класу
City1 = City("Київ", "Київщина", "Україна", "2,8 мільйонів осіб",
               "01000", "044", "260")

City2 = City("Львів", "Львівщина", "Україна", "723 тис",
               "79000", "032", "360")

# Виведення інформації про Місто1
print(f"Назва міста: {City1.get_city_name()}")
print(f"Назва регіону: {City1.get_region()}")
print(f"Назва країни: {City1.get_country_name()}")
print(f"Кількість жителів у місті: {City1.get_population()}")
print(f"Поштовий індекс: {City1.get_postal_code()}")
print(f"Код міста: {City1.get_city_code()}")

# Виведення інформації про Місто2
print(f"Назва міста: {City2.get_city_name()}")
print(f"Назва регіону: {City2.get_region()}")
print(f"Назва країни: {City2.get_country_name()}")
print(f"Кількість жителів у місті: {City2.get_population()}")
print(f"Поштовий індекс: {City2.get_postal_code()}")
print(f"Код міста: {City2.get_city_code()}")