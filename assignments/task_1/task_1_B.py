# Task 1 B

# AI log: not used


def create_file_v2(file_name="myfile.txt"):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("Hello file world!")


def read_file_v2(file_name="myfile.txt"):
    with open(file_name,'r', encoding='utf-8') as file:
        return file.read()



print(read_file_v2())