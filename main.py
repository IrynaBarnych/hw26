# Завдання 4
# Реалізуйте клас «Годинник». Збережіть у класі:
# назву моделі годинника, виробника годинника, рік випуску, ціну годинника, тип годинника (наручний,
# настінний і т. д.). Реалізуйте конструктор та методи класу для введення-виведення даних,
# а також для інших операцій. Використовуйте механізм перевантаження методів.

class Watch:
    def __init__(self, model, manufacturer, year, price, watch_type):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.watch_type = watch_type

    def get_model(self):
        return self.model

    def get_manufacturer(self):
        return self.manufacturer

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    def get_watch_type(self):
        return self.watch_type

watch1 = Watch("Чип", "Швейцарія", 2020, 200, "Ручний")
watch2 = Watch("Дейл", "Китай", 2022, 300, "Настінний")

print(f"Модель: {watch1.get_model()}")
print(f"Виробник: {watch1.get_manufacturer()}")
print(f"Рік випуску: {watch1.get_year()}")
print(f"Цена: {watch1.get_price()}")
print(f"Вид годинника: {watch1.get_watch_type()}")

print(f"Модель: {watch2.get_model()}")
print(f"Виробник: {watch2.get_manufacturer()}")
print(f"Рік випуску: {watch2.get_year()}")
print(f"Цена: {watch2.get_price()}")
print(f"Вид годинника: {watch2.get_watch_type()}")


