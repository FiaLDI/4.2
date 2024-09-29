#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Conversation:
    def __init__(self, first, second):
        """
        Инициализатор класса Conversation.
        first: продолжительность разговора в минутах(целое положительное число)
        second: стоимость одной минуты в рублях(дробное положительное число)
        """
        if not isinstance(first, int) or first <= 0:
            raise ValueError("Поле 'first' должно быть целым положительным числом.")
        if not isinstance(second, (int, float)) or second <= 0:
            raise ValueError("Поле 'second' должно быть положительным числом.")

        self.first = first
        self.second = second

    def cost(self):
        """Вычисление общей стоимости разговора"""
        return self.first * self.second

    def display(self):
        """Вывод данных на экран"""
        print(f"Продолжительность разговора: {self.first} минут")
        print(f"Стоимость одной минуты: {self.second} рубля")
        print(f"Общая стоимость разговора: {self.cost()} рублей")

    def read(self):
        """Ввод данных с клавиатуры"""
        try:
            self.first = int(
                input("Продолжительность в минутах (целое положительное число): ")
            )
            self.second = float(
                input("Введите стоимость минуты в рублях (положительное число): ")
            )
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            return None

    # Перегрузки:
    # Приведение к типам
    def __str__(self):
        return f"{self.first}:{self.second}"

    def __repr__(self):
        return self.__str__

    def __bool__(self):
        return self.first != 0 and self.second != 0

    def __float__(self):
        return self.cost()

    # Математические операции
    def __clone(self):
        return Conversation(self.first, self.second)

    def __iadd__(self, rhs):  # +=
        if isinstance(rhs, Conversation):
            a = self.first + rhs.first
            b = self.second + rhs.second

            self.first, self.second = a, b
            return (a, b)
        else:
            raise ValueError("Illegal Type")

    def __add__(self, rhs):
        return self.__clone().__iadd__(rhs)

    def __isub__(self, rhs):  # -=
        if isinstance(rhs, Conversation):
            a = self.first - rhs.first
            b = self.second - rhs.second

            self.first, self.second = a, b
            return (a, b)
        else:
            raise ValueError("Illegal Type")

    def __sub__(self, rhs):  # -
        return self.__clone().__isub__(rhs)

    def __imul__(self, rhs):  # *=
        if isinstance(rhs, Conversation):
            a = self.first * rhs.first
            b = self.second * rhs.second

            self.first, self.second = a, b
            return (a, b)
        else:
            raise ValueError("Illegal Type")

    def __mul__(self, rhs):  # *
        return self.__clone().__imul__(rhs)

    # Логические операции
    def __eq__(self, rhs):
        """Перегрузка оператора равенства"""
        if isinstance(rhs, Conversation):
            return self.cost() == rhs.cost()

        return NotImplemented

    def __lt__(self, rhs):
        """Перегрузка оператора меньше"""
        if isinstance(rhs, Conversation):
            return self.cost() < rhs.cost()
        return NotImplemented


def make_Conversation(first, second):
    """
    Внешняя функция для создания объекта Conversation.
    Проверяет корректность переданных параметров.
    """
    try:
        return Conversation(first, second)
    except ValueError as e:
        print(f"Ошибка создания объекта: {e}")
        return None


if __name__ == "__main__":
    conv1 = make_Conversation(12, 3.5)
    conv2 = make_Conversation(10, 2.5)

    if conv1 and conv2:
        conv1.display()
        conv2.display()

        # Сравнение объектов
        if conv1 == conv2:
            print("Разговоры имеют одинаковую стоимость.")
        elif conv1 < conv2:
            print("Первый разговор дешевле второго.")
        else:
            print("Первый разговор дороже второго.")

        print(float(conv1))
        print(conv1 - conv2)
        print(conv1 + conv2)
        print(conv1 * conv2)
