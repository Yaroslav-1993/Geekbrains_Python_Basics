first_result = float(input("Введите первый результат >>> "))
target_result = float(input("Введите целевой результат >>> "))
n = 1

while first_result < target_result:
    first_result = first_result * 1.1
    n = n + 1

print(f"Целевой результат будет достигнут на {int(n)}-й день")

