# Task 1

# AI log: not used

def oops():
    # raise IndexError
    raise KeyError


def look_opps():
    try:
        oops()
    except IndexError:
        print("Неверный индекс")


look_opps()

# После изменения oops, а именно замена ошибки с IndexError на KeyError и запуска обработчика ошибок мы получили явную ошибку KeyError
# Получили мы ее из за того что не прописали эту ошибку в обработчике
