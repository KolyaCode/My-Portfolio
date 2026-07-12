import random

balance = 250

def menu():
    print("-----Case opening-----")
    print(f"Баланс: {balance}$")
    print("1. Открыть кейс - 50$")
    print("2. Выход")

case_awards = [25, 50, 100, 250]

def random_awards():
    return random.choice(case_awards)

while True:
    menu()
    users_choose = int(input("Выберите действие: "))
    if users_choose not in [1, 2]:
        print("Такого действия нет!")
        continue
    elif users_choose == 1 and balance >= 50:
        award = random_awards()
        print("Вы открыли кейс!")
        print(f"Вы получили: {award}$")
        balance -= 50
        balance += award
        print(f"Ваш баланс: {balance}$")
    elif balance < 50 and users_choose == 1:
        print("Недостаточно денег :(")
        break
    elif users_choose == 2:
        print("Выход.....")
        break








