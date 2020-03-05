    """
    Функция принимает пароль строкой и выполняет валидацию с помощью трёх
    вспомогательных функций:
    1. Содержит только a−z, A−Z, 0−9
    2. Содержит четное количество букв
    3. Содержит нечетное количество цифр
    Основная функция возвращает True, если пароль валидный.
    Если пароль не валидный, возвращает лист стрингов, в которых перечислены
    причины неуспешной проверки. Например: ["содержит запрещенные символы"]
    """
def characters(password):

    if password.islower():
        print ('Пароль содержит буквы только в нижнем регистре!')

    elif password.isupper():
        print ('Пароль содержит буквы только в верхнем регистре!')

    elif password.isdigit():
        print ('Пароль содержит только цифры!')
    return True


def count_letters(password):

    password = password.lower()
    counting = 0
    for i in password:
        if i in "aeiouybcdfghjklmnpqrstvwxz":
            counting += 1

    return True if counting % 2 == 0 else print ("Пароль должен содержать четное количество букв!")


def count_numbers(password):

    counting = 0
    for i in password:
        if i in "1234567890":
            counting += 1

    return True if counting % 2 != 0 else print ("Пароль должен содержать нечетное количество цифр!")


def validate_password(password):

    if characters(password):
        if count_letters(password):
            if count_numbers(password):
                return True

password = input()
validate_password(password)


    """
    Функция принимает число и конвертирует его в 4 форматах:
    decimal, octal, binary, hexadecimal. Каст в форматы описан в документации.
    При касте нужно избавляться от первых символов (0o31 -> 31, 0xe6 -> e6).
    Возвращает строку, отформатированную с помощью функции print_table.
    """

def int_converter(input_int):
    a = str(input_int), oct(input_int)[2:], bin(input_int)[2:], hex(input_int)[2:]
    return ", ".join(a)

input_int = int(input())
print(int_converter(input_int))



    """
    Функция генерирует псевдотаблицу текстом.
    :cols: количество колонок в таблице
    :rows: количество строк в таблице
    :*data: лист листов, где каждый вложенный лист - строка данных.
    Пример: print_table(cols=4, rows=2, [["Decimal", "Octal", "Binary", "Hexadecimal"], [230, 346, 11100110, "e6"]])
    Вернет строку вида:
     -----------------------------------------------------------
    | Decimal      | Octal        | Binary       | Hexadecimal  |
    | 230          | 346          | 11100110     | e6           |
     -----------------------------------------------------------
    Форматирование должно полностью совпадать с примером.
    Обратить внимание на размеры ячеек - 12 символов на текст + по 1 вокруг
    слева и справа от разделителя |.
    """


def print_table(cols=1, rows=1, *data):

    print((" {:->" + str(cols * 14) + "}").format("-"))

    a = ["| ".join(i).split(",") for i in data]
    for i in a:
        for k in i:
            print("{}{:<12}{}".format("| ", str(k), " |"))
            
    print((" {:->" + str(cols * 14) + "}").format("-"))

print_table(cols=3, rows=1, (["Decimal", "Octal", "Binary", "Hexadecimal"], ["230", "346", "11100110", "e6"]))