#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime


class Bill:
    def __init__(self, phone_number, last_name, payment_date, payment_amount, paid):
        self.phone_number = phone_number
        self.last_name = last_name
        self.payment_date = payment_date
        self.payment_amount = payment_amount
        self.paid = paid


class ListPayer:
    MAX_SIZE = 100  # Константа максимального размера списка

    def __init__(self, size):
        self.size = min(size, self.MAX_SIZE)
        self.count = 0
        self.payers = []

    def show(self, idx = -1):
        print('__Начало вывода__')
        if self.payers != 0:
            for i, item in enumerate(self.payers):
                if (idx < 0):
                    print(
                        f"{i} | {item.phone_number} {item.last_name} {item.payment_date.date()} {item.payment_amount} {item.paid}"
                    )
                else:
                    if i == idx:
                        print(
                            f"{i} | {item.phone_number} {item.last_name} {item.payment_date.date()} {item.payment_amount} {item.paid}"
                        )
        print('__конец вывода__')
                

    def size(self):
        return self.size

    def add_payer(self, payer):
        if self.count < self.size:
            self.payers.append(payer)
            self.count += 1
        else:
            print("Список полон")

    def remove_payer(self, phone_number):
        for payer in self.payers:
            if payer.phone_number == phone_number:
                self.payers.remove(payer)
                self.count -= 1
                break

    def find_by_phone(self, phone_number):
        for i, item in enumerate(self.payers):
            if item.phone_number == phone_number:
                self.show(i)

    def find_by_last_name(self, last_name):
        for i, item in enumerate(self.payers):
            if item.last_name == last_name:
                self.show(i)

    def total_payment_amount(self):
        return sum(payer.payment_amount for payer in self.payers)

    def union(self, other_list):
        new_list = ListPayer(self.size + other_list.size)
        new_list.payers = list(set(self.payers) | set(other_list.payers))
        new_list.count = len(new_list.payers)

        new_list.show()
        return new_list

    def intersection(self, other_list):
        new_list = ListPayer(self.size)
        new_list.payers = list(set(self.payers) & set(other_list.payers))
        new_list.count = len(new_list.payers)

        new_list.show()
        return new_list

    def generate_group(self, filter_func):
        group = Group()
        group.payers = list(filter(filter_func, self.payers))
        return group


class Group:
    def __init__(self):
        self.payers = []


if __name__ == "__main__":
    # Пример использования:
    payer1 = Bill("1234567890", "Ivanov", datetime(2024, 10, 24), 100, True)
    payer2 = Bill("0987654321", "Petrov", datetime(2024, 10, 23), 150, False)

    list_payer = ListPayer(10)
    list_payer.add_payer(payer1)
    list_payer.add_payer(payer2)

    # Поиск по телефону
    list_payer.find_by_phone('0987654321')

    list_payer.find_by_last_name('Petrov')

    #Выводим общую сумму платежей
    print("Общаа сумма:", list_payer.total_payment_amount())

    payer21 = Bill("0987654321", "Ivanov", datetime(2024, 10, 24), 100, True)

    list_payer2 = ListPayer(10)
    list_payer2.add_payer(payer21)

    # Логические операции

    list_payer.union(list_payer2)



    