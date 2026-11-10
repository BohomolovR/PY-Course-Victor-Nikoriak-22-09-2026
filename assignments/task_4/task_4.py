# Task 4

# AI log: not used

import json

def load(path):
    try:
        with open(path, 'r', encoding='utf-8') as json_file:
            records = json.load(json_file)
        return records
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found in {path!r}")


def save(path,records):
    with open(path,'w',encoding='utf-8') as json_file:
        json.dump(records, json_file, indent=2)

def add_books(records, new_book):
    records.append(new_book)
    return records


def list_book(records):
    for record in records:
        print(
            f"ID: {record["id"]}\n"
            f"Title: {record["title"]}\n"
            f"Author: {record["author"]}\n"
            f"Read: {'Read' if record['is_read'] else 'Not read'}\n"
        )


def remove_book(records,book_id):
    for record in records:
        if record["id"] == book_id:
            records.remove(record)
            return True
    return False


def main():
    path = "books.json"
    records = load(path)

    while True:
        print(
            "\n1. Add a book\n"
            "2. List books\n"
            "3. Remove a book\n"
            "0. Save and exit"
        )
        option = input("Choose an option: ").strip()

        if option == "1":
            title = input("Title: ").strip()
            author = input("Author: ").strip()

            if not title or not author:
                print("Title and author cannot be empty.")
                continue

            while True:
                answer = input("Have you read this book? (yes/no): ").strip().lower()
                if answer in ("yes", "no"):
                    break
                print("Please enter yes or no.")

            new_book = {
                "id": max((record["id"] for record in records), default=0) + 1,
                "title": title,
                "author": author,
                "is_read": answer == "yes"
            }
            add_books(records, new_book)
            print("Book added.")

        elif option == "2":
            if records:
                list_book(records)
            else:
                print("No books found.")

        elif option == "3":
            list_book(records)
            try:
                book_id = int(input("Book ID to remove: "))
            except ValueError:
                print("Please enter a numeric ID.")
                continue

            if remove_book(records, book_id):
                print("Book removed.")
            else:
                print("Book not found.")

        elif option == "0":
            save(path, records)
            print("Books saved.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
