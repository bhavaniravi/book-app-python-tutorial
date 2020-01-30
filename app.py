import csv


def list_books():
    # Opens the file in reading and writing mode
    with open('books.csv', mode='r') as f:
        rows = csv.DictReader(f)

        for row in rows:
            print("\n")
            print("Book Name :: " + row["BookName"])
            print("Author :: " + row["Author"])
            print("Read :: " + row["Read"])
            print("SharedWith :: " + row["SharedWith"])


def update_book():
    # 5.1
    book_name = input("Enter book name ::")

    # 5.2
    is_book_read = input("Book Read (Y/N)?")

    if is_book_read == "Y":
        is_book_read = True

    elif is_book_read == "N":
        is_book_read = False

    # 5.3
    import csv
    rows = []

    # Opens the file in reading and writing mode
    with open('books.csv', mode='r') as f:
        rows = list(csv.DictReader(f))

        # 5.4
        for row in rows:
            if row["BookName"] == book_name:
                row["Read"] = is_book_read
                break

    with open('books.csv', mode='w') as f:
        csv_writer = csv.DictWriter(
            f, fieldnames=["BookName", "Author", "Read", "SharedWith"])
        csv_writer.writerows(rows)

    print("Book Successfully Updated")


def add_book():
    # 4.1
    book_name = input("Enter book name")
    author = input("Enter Author name")

    # 4.2
    import csv
    # Opens the file in writing mode

    with open('books.csv', mode='a') as f:
        writer = csv.DictWriter(f, fieldnames=[
            "BookName", "Author", "Read", "SharedWith"])
        writer.writerow({"BookName": book_name,
                         "Author": author})

    print("Book Successfully Added")


print("Menu ::")
print("1. Add Book")
print("2. Update Book")
print("3. Share Book")
print("4. List Book")


choice = int(input("Enter your option ::"))

if choice == 1:
    add_book()

elif choice == 2:
    update_book()

elif choice == 3:
    share_book()

elif choice == 4:
    list_books()
