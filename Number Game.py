import random

def random_number_function():
    return random.randint(1,10)

random_number = random_number_function()

print("Добро пожаловать в игру - Угадай число")
print("У вас будет 5 попыток")
print("Вам нужно угадать число от 1 до 10")

attempts = 5

try:
    while attempts > 0:
        user_number = int(input("Введите число: "))
        if user_number == random_number:
            print("Вы угадали число!")
            print("Выход....")
            break
        elif user_number != random_number and attempts != 0:
            attempts -= 1
            if attempts == 0:
                print("У вас закончились попытки! Игра окончена!")
                print("Выход....")
                break
            print("Неверно! Попробуйте еще!")
            print(f"Осталось попыток: {attempts}")

except ValueError:
    print("Ввод должен быть числом!")
    print("Выход....")
