import math


class Figure:
    def __init__(self):
        pass


class Point(Figure):
    def __init__(self):
        super().__init__()
        self.x = input_check(txt_x)
        self.y = input_check(txt_y)

    def get(self):
        return self.x, self.y


class Triangle(Figure):
    def __init__(self):
        super().__init__()
        self.name = "треугольник"
        self.a = Point().get()
        self.b = Point().get()
        self.c = Point().get()
        self.ab = math.dist(self.a, self.b)
        self.bc = math.dist(self.b, self.c)
        self.ac = math.dist(self.a, self.c)
        self.per = self.ab + self.bc + self.ac
        self.half_p = self.per / 2
        self.ar = math.sqrt(self.half_p * (self.half_p - self.ab) * (self.half_p - self.bc) * (self.half_p - self.ac))

    def __str__(self):
        return f"Треугольник, со сторонами {round(self.ab, 2)}, {round(self.bc, 2)}, {round(self.ac, 2)}"

    def ans(self):
        return f"Треугольник с площадью {round(self.ar, 2)}"

    def perimeter(self):
        return f"Периметр треугольника равен {round(self.per, 2)}"

    def area(self):
        return f"Площадь треугольника равна {round(self.ar, 2)}"


class Circle(Figure):
    def __init__(self):
        super().__init__()
        self.name = "круг"
        self.o = Point().get()
        self.r = float(input_check(txt_r))
        self.per = 2 * math.pi * self.r
        self.ar = math.pi * self.r ** 2

    def __str__(self):
        return f"Круг, с центром в точке {self.o} и радиусом {self.r}"

    def ans(self):
        return f"Крут с площадью {round(self.ar, 2)}"

    def perimeter(self):
        return f"Периметр круга равен {round(self.per, 2)}"

    def area(self):
        return f"Площаль круга равна {round(self.ar, 2)}"


class Quadrilateral(Figure):
    def __init__(self):
        super().__init__()
        self.name = "четырёхугольник"
        self.a = Point().get()
        self.b = Point().get()
        self.c = Point().get()
        self.d = Point().get()
        self.ab = math.dist(self.a, self.b)
        self.bc = math.dist(self.b, self.c)
        self.cd = math.dist(self.c, self.d)
        self.da = math.dist(self.d, self.a)
        self.per = self.ab + self.bc + self.cd + self.da
        self.h_p = self.per / 2
        self.ar = math.sqrt((self.h_p - self.ab) * (self.h_p - self.bc) * (self.h_p - self.cd) * (self.h_p - self.da))

    def __str__(self):
        return f"Четырёхугольник, со сторонами {round(self.ab, 2)}, " \
               f"{round(self.bc, 2)}, {round(self.cd, 2)}, {round(self.da, 2)}"

    def ans(self):
        return f"Четырёхугольник с площадью {round(self.ar, 2)}"

    def perimeter(self):
        return f"Периметр четырёхугольника равен {round(self.per, 2)}"

    def area(self):
        return f"Площадь четырёхугольника равна {round(self.ar, 2)}"


def input_check(txt):  # обработчик ошибок ввода
    while True:
        try:
            number = float(input(txt))
            if int(number) <= 0:
                print("Введите число!")
            else:
                return number
        except ValueError:
            print("Некоректное значение, попробуйте ещё раз")


def out(fig):
    print("--------------------")
    print(fig)
    print(fig.perimeter())
    print(fig.area())
    print("--------------------")
    return None


txt_1 = "Введите цифру\n1 - создать фигуры\n2 - очистить список фигур\n3 - заверишить работу\n: "
txt_2 = "Введите цифру\n1 - создать треугольник\n2 - создать круг\n3 - создать четырёхугольник\n: "
txt_3 = "Сколько фигур вы хотите создать?: "
txt_r = "Введите радиус окружности: "
txt_x = "Введите х координату точки: "
txt_y = "Введите y координату точки: "

areas = []
a = 0
while a != 3:
    a = int(input_check(txt_1))
    if a == 1:
        c = int(input_check(txt_3))
        for i in range(c):
            b = int(input_check(txt_2))
            if b == 1:
                figure = Triangle()
                areas.append(figure)
                out(figure)
            elif b == 2:
                figure = Circle()
                areas.append(figure)
                out(figure)
            elif b == 3:
                figure = Quadrilateral()
                areas.append(figure)
                out(figure)
        areas.sort(key=lambda x: x.ar, reverse=True)
        print("Отсортированный по площади список фигур от большего к меньшему: ")
        for i in range(len(areas)):
            print(areas[i].ans())
    elif a == 2:
        areas = []
