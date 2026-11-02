# Task 5


# AI log: not used

def total_of(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


print(total_of([1, 2, 3, 4, 5, 6]))

# Traceback (most recent call last):
#   File "/Users/rostyslav/beetroot_homework/homework-try:except/task_5.py", line 12, in <module>
#     print(total_of([1, 2, 3, 4, 5, 6]))
#           ~~~~~~~~^^^^^^^^^^^^^^^^^^^^
#   File "/Users/rostyslav/beetroot_homework/homework-try:except/task_5.py", line 8, in total_of
#     total += nubmer
#              ^^^^^^
# NameError: name 'nubmer' is not defined


# Я считаю что try/except здесь в принципе не нужен,
# пуйскай ошибку перехватит вызывающий код и то здесь была проблема
# в неправильном названии переменой, так что нужен ли он тут вообще.

# При старом коде можно запускать даже не десятью тысячью записей, а милионом
# записей все равно перенная total не изменится и будет равна 0
