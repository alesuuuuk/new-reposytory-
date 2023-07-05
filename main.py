if __name__ == "__main__":
    # task 1
    stAction = input("для того, щоб додати числа - напишіть 1, добуток - 2")
    if stAction == "1":
        a = int(input("число 1"))
        b = int(input("число 2"))
        c = int(input("число 3"))
        print(a+b+c)
    elif stAction == "2":
        a = int(input("число 1"))
        b = int(input("число 2"))
        c = int(input("число 3"))
        print(a*b*c)
    else:
        print("введіть правильне число")

    # task 2

    ndAction = input("для того щоб дізнатись найбільше число - 1, найменше - 2, череднє арифметичне - 3")
    if ndAction == "1":
        a = int(input("число 1"))
        b = int(input("число 2"))
        c = int(input("число 3"))
        maxNumber = max(a, b, c)
        print(maxNumber)
    elif ndAction == "2":
        a = int(input("число 1"))
        b = int(input("число 2"))
        c = int(input("число 3"))
        minNumber = min(a, b, c)
        print(minNumber)
    elif ndAction == '3':
        a = int(input("число 1"))
        b = int(input("число 2"))
        c = int(input("число 3"))
        print(a*b*c/3)
    else:
        print("введіть нормальне чсило ")

    # task 3

    metres = int(input("Введіть скільки вам потрібно перевести метрів"))
    rdAction = input("1 - в дюйми, 2 - ярди 3 - в милі")
    if rdAction == "1":
        print(metres*39.370, "дюймів")
    elif rdAction == "2":
        print(metres*1.0936, "ярдів")
    elif rdAction == "3":
        print(round(metres*0.00062137119609836, 3), "миль")
    else:
        print("введіть нормальне чсило ")
