# Task 1 A

# AI log: not used


def create_file(file_name="myfile.txt"):
    file = open(file_name, 'w', encoding='utf-8')
    file.write("Hello file world!")
    file.close()


def read_file(file_name="myfile.txt"):
    file = open(file_name,'r',encoding='utf-8')
    text = file.read()
    file.close()
    return text


create_file()
print(read_file())
