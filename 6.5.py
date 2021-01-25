# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
# “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self,title = "Just draw."):
        self.title = title


    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Blue line.")


class Pencil(Stationery):
    def draw(self):
        print("Thin black line.")


class Handle(Stationery):
    def draw(self):
        print("Thick orange line.")


pen = Pen()
pen.draw()

crayon = Pencil()
crayon.draw()

stabilo = Handle("Your favourite marker.")
stabilo.draw()