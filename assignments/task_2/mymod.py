# Task 2

# AI log: not used



def count_lines(name):
    with open(name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return len(lines)

def count_chars(name):
    with open(name, 'r', encoding='utf-8') as f:
        all_chars = f.read()
    return len(all_chars)



print(count_lines('mymod.py'))
print(count_chars('mymod.py'))


# rostyslav@mac homework-file % python3 mymod.py
# 23
# 352
# rostyslav@mac homework-file % wc -l -c mymod.py
#       23     352 mymod.py
# rostyslav@mac homework-file %

