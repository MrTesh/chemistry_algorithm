print("Введите номер периода")
orbits = int(input())  # 4
print("Введите номер группы")
last_orb_e = int(input())  # 2
print("Введите порядковый номер элемента")
e = int(input())  # 20

answer = [last_orb_e]
e -= last_orb_e
for i in range(1, orbits + 1):
    if e > 2 * i ** 2:
        answer.append(2 * i ** 2)
        e -= 2 * i ** 2
    elif e <= 2 * i ** 2:
        answer.append(e)
        break

answer += [answer.pop(0)]
for i in answer:
    print(i, end=" ")




