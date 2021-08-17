earnings = float(input("Введите сумму выручки в рублях >>> "))
costs = float(input("Введите сумму издержек в рублях >>> "))

if costs > earnings:
    print("Убыток")
elif costs == earnings:
    print("В ноль")
else:
    print(f"Прибыль = {int((earnings-costs)/costs*100)}%")

empl_nmbr = float(input("Введите численность сотрудников >>> "))

print(f"Прибыль на сотрудика = {round(float((earnings-costs)/empl_nmbr), 3)}, руб.")