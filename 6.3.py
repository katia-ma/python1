# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return print(f"Worker's name: {self.name} {self.surname}")

    def get_total_income(self):
        return print(f"Worker's total income {sum(self._income.values())}")


junior = Position("Peter", "Brown", "barista", 700, 20)
junior.get_full_name()
junior.get_total_income()
boss = Position("Anne", "Parker", "PR director", 3000, 500)
boss.get_full_name()
boss.get_total_income()
