# Task 3

# AI log: not used

def count_lines(lines):
    return len(lines)


def count_chars(lines):
    all_chars = 0
    for item in lines:
        all_chars += len(item)
    return all_chars


def test(lines):
    all_lines = count_lines(lines)
    all_chars = count_chars(lines)
    print(f"Всего строк: {all_lines}\n"
          f"Всего символов: {all_chars}")


if __name__ == "__main__":
    test(["Привет", "Как дела?", "Пока"])
