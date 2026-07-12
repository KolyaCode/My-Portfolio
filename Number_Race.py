import random

user_number = 0
final_number = 100


def random_number():
    calculate = random.choice(["+", "-", "*"])
    number1 = random.randint(1, 20)

    return calculate, number1


def menu():
    print("Добро пожаловать в игру Number Race!")
    print("Ваша цель дойти до 100")
    print(f"Ваше число: {user_number}")


while user_number < final_number:

    menu()

    option1 = random_number()
    option2 = random_number()

    print(f"1: {option1[0]} {option1[1]}")
    print(f"2: {option2[0]} {option2[1]}")

    user_choice = input("Выберите вариант 1 или 2: ")

    if user_choice == "1":
        operation = option1
    elif user_choice == "2":
        operation = option2
    else:
        print("Неверный выбор")
        continue


    symbol = operation[0]
    number = operation[1]


    if symbol == "+":
        user_number += number

    elif symbol == "-":
        user_number -= number

    elif symbol == "*":
        user_number *= number


    print(f"Теперь ваше число: {user_number}")


print("Поздравляем! Вы дошли до 100!")