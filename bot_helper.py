# -*- coding: utf-8 -*-
"""
Console Bot helper.
For add, change, get phone numbers with wrapper of errors (@decorator)
"""
import re


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give me correct phone please."
        except IndexError:
            return "Add phone in correct format."
        except TypeError:
            return "Check format"
        except:
            return "Unexpected error, pls try one more time"
    return wrapper


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts, additional='added'):
    name, phone = args
    reg_phone = ''.join(re.findall(r'[\+\(]?[1-9]', phone))
    if additional == "updated" and name not in contacts:
        return f"Contact '{name}' is not in contact list"
    if reg_phone:
        contacts[name] = reg_phone
    else:
        return f"Looks like your phone number '{phone}' in incorrect format try one more time"
    return f"Contact {additional}."


@input_error
def show_phone(args, contacts):
    phone = contacts[args[0]]
    return f"Phone number for {args[0]} is {phone}"


@input_error
def get_all(contacts):
    if contacts:
        return '\n'.join([f"{k}: {v}" for k, v in contacts.items()])
    else:
        return "Data is empty, nothing to show"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(add_contact(args, contacts, "updated"))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(get_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
