# Task 3

# AI log: Not used


from functools import wraps


def string_arg_rules(max_length=1, contains=(), exclude=()):
    def decorator(func):
        @wraps(func)
        def examination(*args, **kwargs):
            for value in args:
                if not isinstance(value, str):
                    raise TypeError("Аргумент должен быть строкой")
                if not (len(value) <= max_length):
                    raise ValueError(f"Превышенно максимальное количество символов {max_length!r}")
                for item in contains:
                    if item not in value:
                        raise ValueError(f"Аргумент должен содержать {item!r}")
                for item in exclude:
                    if item in value:
                        raise ValueError(f"Аргумент не должен содержать {item!r}")
            return func(*args, **kwargs)

        return examination

    return decorator


@string_arg_rules(max_length=15, contains=('05', '@'), exclude=("S", 's'))
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == "__main__":
    create_slogan('peter@05')  # Всё в порядке
    create_slogan('peter@06')  # ValueError: аргументы должны содержать '05'
    create_slogan('Seter@05')  # ValueError: аргументы не должны содержать 'S'
