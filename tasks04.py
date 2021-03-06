# 1. Написать свой cache декоратор c максимальным размером кеша и его очисткой
# при необходимости.

def do_cache(maxsize):
    def decorator(func):
        cache = list() # этот лист будет доступен при следующих вызовах
        def wrapper(*args):
            if len(cache) >= maxsize:
                # Если количество закешированных элементов превышает maxsize,
                # нужно удалить самый первый закешированный элемент.
                cache.pop([0])
            if args in cache:
                # Если элемент уже есть в кеше, нужно вернуть его, не вызывая
                # декорируемой функции
                return args
            else:
                # Если элемента нет в кеше, нужно вызвать декорируемую функцию,
                # сохранить ее результат в кеш и вернуть ее результат
                cache.append(func(*args))
                return func(*args)
        return wrapper
    return decorator


@do_cache(maxsize=2)
def test(v, i):
    return v + i


# 2. Написать свой декоратор который будет проверять остаток от деления числа 100
# на результат работы функции ниже. Если остаток от деления = 0, вывести
# сообщение "We are OK!», иначе «Bad news guys, we got {остаток от деления}».
# Этот декоратор не должен возвращать результат работы функции. Только один из
# указанных принтов.

def div100(func):
    def wrapper(*args):
        # your code here
        result = 100 % func(*args)
        if result == 0:
            print("We are OK!")
        else:
            print(f"Bad news guys,we got of {result}")
        
    return wrapper


@div100
def test2(v):
    return v

# 3. Декоратор должен кэшировать значения аргументов, считать количество
# использований одних и тех же аргументов и печатать их перед исполнением
# декорируемой функции.


def count_args(func):
    cache = list() # этот дикт будет доступен при следующих вызовах
    cache_count = dict() # этот дикт будет доступен при следующих вызовах
    def wrapper(*args):
        # your code here
        cache.append(func(*args))
        cache_count = {key: cache.count(key) for key in cache}
        print(cache_count)
    return wrapper


@count_args
def my_func(string):
    return string
