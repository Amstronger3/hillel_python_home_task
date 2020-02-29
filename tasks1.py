def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    # your code here
    result_list = [i for i in url_list if i.count("/catalog/")]
    return result_list

url_list = ["https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html","https://pythonworld.ru/catalog/vstroennye-funkcii.html"]
print(catalog_finder(url_list))


def idiotic_str(input_str):
    """
    Вернуть полученную строку, сделав каждую вторую букву заглавной:
    Пример: тестовая строка -> тЕсТоВаЯ СтРоКа
    """
    # your code here
    idiotic_str = str()
    for i,c in enumerate(input_str):
        idiotic_str += c if i%2 == 0 else c.upper()
    
    return idiotic_str

input_list = input()
print(idiotic_str(input_list))


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    # your code here
    output_str = str()
    if len(input_str) >= 2:
        output_str = input_str
        if len(input_str) %2 == 0:
            return input_str[len(input_str)//2 - 1:len(input_str)//2 + 1]
        else:
            return input_str[len(input_str)//2 - 1:len(input_str)//2 + 2]
    else:
        print("Строка может принимать не меньше двух символов")
    return output_str

input_str = input()
print(get_str_center(input_str))


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    # your code here
    output_dict = dict()
    input_str = input_str.lower()
    for i in input_str:
        output_dict[i] = input_str.count(i)
    
    return output_dict

input_str = input()
print(count_symbols(input_str))


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    # your code here
    result_str = str(str1[:len(str1)//2]+str2+str1[len(str1)//2:])
    return result_str

str1 = input()
str2 = input()
print(mix_strings(str1,str2))


def avg_score(score_list):
    """
    Дописать функцию, которая принимает список строк с оценками, а возвращает
    список строк со средним баллом
    Пример: ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"] ->
    ["Mike|65", "Jane|42"]
    """
    # your code here
    avg_scores = None
    return avg_scores


def encrypt_str(input_str):
    """
    Дописать функцию, которая будет шифровать полученную строку следующим
    образом:
    Пример 1: "www" -> "w3"
    Пример 2: "abbbccdeffgggg" -> "ab3c2def2g4"
    """
    # your code here
    encrypted_str = None
    return encrypted_str


def squared_dict(input_dict):
    """
    Сгенерировать dict() из списка ключей ниже по формуле (key : key*key).
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
    """
    # your code here
    squared_dict = {input_dict[i]: input_dict[i]**2 for i in range(0, len(input_dict), 1)}
    return squared_dict

input_dict = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(squared_dict(input_dict))


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    # your code here
    even_int_list = list( i for i in range( 0, 101 ) if i % 2 == 0 )
    return even_int_list

print(even_int_generator())


def replace_vowels(input_str):
    """
    Заменить в произвольной строке согласные буквы на гласные.
    """
    # your code here
    result_str = None
    return result_str

input_str = input()
print(replace_vowels(input_str))


def filter_unique_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    убрать из него повторяющиеся элементы
    """
    # your code here

    unique_int_list = set(list(input_list))
    return unique_int_list

input_str = input()
print(filter_unique_int(input_str))


def three_biggest_int(input_list):
    """
    Дан массив чисел.
    
    вывести 3 наибольших числа из исходного массива
    """
    # your code here
    input_list = sorted(input_list)
    biggest_ints = input_list[-3:]
    return biggest_ints

input_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
print(three_biggest_int(input_list))


def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """
    # your code here
    lowest_int_index = input_list.index(min(input_list))
    return lowest_int_index

input_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
print(lowest_int_index(input_list))


def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    # your code here
    input_list.reverse()
    reversed = input_list
    return reversed

input_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
print(reversed_list(input_list))


def find_common_keys(dict1, dict2):
    """
    Найти общие ключи в двух словарях, вернуть список их названий
    """
    common_keys = list(set(dict1.keys())&set(dict2.keys()))
    return common_keys

dict1 = dict(a=1,b=2,c=3)
dict2 = dict(d=4,e=5,c=6)

print(find_common_keys(dict1,dict2))


def sort_by_age(student_list):
    """
    Дан массив из словарей. C помощью sort() отсортировать массив из словарей
    по значению ключа 'age', сгруппировать данные по значению ключа 'city'
    вывод должен быть такого вида :
        {
           'Kiev': [ {'name': 'Viktor', 'age': 30 },
                        {'name': 'Andrey', 'age': 34}],
           'Dnepr': [ {'name': 'Maksim', 'age': 20 },
                           {'name': 'Artem', 'age': 50}],
           'Lviv': [ {'name': 'Vladimir', 'age': 32 },
                        {'name': 'Dmitriy', 'age': 21}]
        }
    """
    # your code here

    
    sorted_dict = None
    return sorted_dict