
balance = 0

def menu():
    print("-----BANK-----")
    print(f"Выш баланс: {balance}")
    print("1. Выход из банка")
    print("2. Пополнить баланс")
    print("3. Снять деньги")

while True:
    menu()
    user_choice = int(input("Выберите действие, чтобы продолжить: "))
    if user_choice == 1:
        print("Выход....")
        break
    elif user_choice == 2:
        try:
            user_pay = int(input("Введите нужную сумму: "))
            if user_pay > 0:
                balance += user_pay
                print("Вы поплнили свой баланс!")
                print(f"Теперь ваш баланс: {balance}")
                continue
            elif user_pay < 0:
                print("Сумма должа быть больше нуля!")
                continue
        except ValueError:
            print("Ввод должен быть числом!")
            continue
    elif user_choice == 3:
         try:
            user_pay2 = int(input("Введите сумму, которую хотите снять: "))
            if user_pay2 <= 0:
                print("Сумма должна быть больше 0!")
                continue
            elif user_pay2 <= balance:
                balance -= user_pay2
                print("Вы сняли деньги! Ваш баланс обновился!")
                continue
            elif user_pay2 > balance:
                print("Сумма превышает ваш баланс!")
                continue
         except ValueError:
                print("Неккоректный ввод!")
                continue
    else:
        print("Неккоректный ввод!")
        continue