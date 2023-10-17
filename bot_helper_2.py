# -*- coding: utf-8 -*-
"""
AddressBook in classes implementation
Also wrapper of unexpected errors was added for each def inside classes
"""

from collections import UserDict


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            print(f"Unexpected action: {ex} in def {func.__name__}()")
    return wrapper


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, *args, **kwargs):
        super(Name, self).__init__(*args, **kwargs)


class Phone(Field):

    def __init__(self, *args, **kwargs):
        super(Phone, self).__init__(*args, **kwargs)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    @input_error
    def _search_by_phone(self, number):
        for i, phone in enumerate(self.phones):
            if number == phone.value:
                return i, phone
        else:
            return None

    @input_error
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    @input_error
    def delete_phone(self, phone):
        i, _ = self._search_by_phone(phone)
        return self.phones.pop(i)

    @input_error
    def edit_phone(self, old, new):
        i, _ = self._search_by_phone(old)
        self.phones[i] = Phone(new)

    @input_error
    def find_phone(self, number):
        _, number = self._search_by_phone(number)
        return number

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    @input_error
    def add_record(self, record):
        self.update(**{record.name.value: record})

    @input_error
    def find(self, name):
        return self.get(name)

    @input_error
    def delete(self, name):
        return self.pop(name)
