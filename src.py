import mysql.connector as sq
from mysql.connector import Error as sqlerror
from prettytable import PrettyTable
from getpass import getpass

book_headings = ['ID', 'Book Name', 'Author',
                 'Price', 'Catalouge', 'Genre', 'Book Holder']
magazine_headings = ['Magazine Name', 'Genre', 'Quantity']


def establish_conn():
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='library')
    cursor = conn.cursor()

    return conn, cursor


def quit_program():
    print(f"\nThank you for using our program")
    exit()


def validate_change_password():
    print(f"You chose to change your password")
    present_username = input(f"Enter your username : ")
    present_password = getpass("\nEnter your present password : ")
    check = validate_password(present_username, present_password)
    if check:
        change_password(present_username)
    else:
        print("You have entered an invalid combination of username and password. Please Try Again")
        return None


def change_password(username):
    print(f"You can now proceed to change your password")
    while True:
        print(f"The password your enter won't be displayed for security reasons")
        password_input = getpass("Please enter your new password : ")
        second_input = getpass("Please enter the new password again : ")

        if password_input == second_input:
            conn, cursor = establish_conn()
            cursor.execute(
                f"UPDATE users SET password = '{password_input}' WHERE username = '{username}'")
            conn.commit()
            conn.close()
            print(f"You have successfully changed your password")
            return None

        else:
            print(f"The entered password does not match. Please Try Again")
            continue


def validate_password(username, password):
    conn, cursor = establish_conn()
    try:
        cursor.execute(
            f"SELECT name, password FROM users WHERE username = '{username}'")
        db_name, db_password = cursor.fetchone()

    except sqlerror:
        return None
    if db_password == password:
        return db_name
    else:
        return None


def show_book_table():
    conn, cursor = establish_conn()
    cursor.execute(f"SELECT * FROM books")
    d = cursor.fetchall()
    conn.close()
    table = PrettyTable()
    table.field_names = book_headings

    for i, n, a, p, c, g, h in d:
        table.add_row([i, n, a, p, c, g, h])

    print(f"\n{table}\n")
    return None


def show_magazine_table():
    conn, cursor = establish_conn()
    cursor.execute(f"SELECT * FROM magazines")
    d = cursor.fetchall()
    conn.close()
    table = PrettyTable()
    table.field_names = magazine_headings

    for n, g, q in d:
        table.add_row([n, g, q])

    print(f"\n{table}\n")
    return None


def get_one_book_details(book_id):
    conn, cursor = establish_conn()
    cursor.execute(f"SELECT * FROM books WHERE id = {book_id}")
    d = cursor.fetchall()
    conn.close()
    if d == []:
        return None

    else:
        table = PrettyTable()
        table.field_names = book_headings

        for i, n, a, p, c, g, h in d:
            table.add_row([i, n, a, p, c, g, h])

        return table


def update_single_table(dl, table):
    table.add_row(['-', 'Changed to', 'Changed to',
                   'Changed to', 'Changed to', 'Changed to', 'Changed to'])
    table.add_row(dl)

    return table


def complete_update(dl):
    conn, cursor = establish_conn()
    try:
        cursor.execute(
            f"UPDATE books SET name='{dl[1]}', author='{dl[2]}', price={dl[3]}, catalouge='{dl[4]}', genre='{dl[5]}', holder='{dl[6]}' WHERE id ={dl[0]}")
        conn.commit()
        return True

    except sqlerror:
        print(f"An error occurred while updating the data. Please Try Again")
        return None


def update_book_details():
    while True:
        print(f"<<<<< UPDATE BOOK DATA >>>>>")
        id_input = input(f"\nEnter the book id : ")
        before_table = get_one_book_details(id_input)
        if before_table:
            print(f"Previous data of Book Id <{id_input}>\n{before_table}\n")
            new_name = input("Enter the new book name : ")
            new_author = input("Enter the author name : ")
            new_price = input("Enter the new price : ")
            new_catalouge = input("Enter the new calalouge id : ")
            new_genre = input("Enter the new genre : ")
            print(f"NOTE : If there is no book holder enter <None>")
            new_holder = input("Enter the new book holder : ")
            if new_holder == 'None' or new_holder == 'none':
                new_holder = None
            confirm_input = input(
                f"Are you sure you want to update (Y / N) : ")
            if confirm_input in ['Y', 'y']:
                dl = [id_input, new_name, new_author, new_price,
                      new_catalouge, new_genre, new_holder]
                check_var = complete_update(dl)
                if check_var:
                    table = update_single_table(dl, before_table)
                    print(table)
                    return None
                else:
                    return None
            else:
                print(f"You chose not to update the data")
                return None

        else:
            print("The entered book id is not valid. Please Try Again\n")
            continue


def complete_insert(dl):
    conn, cursor = establish_conn()
    try:
        cursor.execute(
            f"INSERT INTO books VALUES ({dl[0]},'{dl[1]}','{dl[2]}',{dl[3]},'{dl[4]}','{dl[5]}','{dl[6]}')")
        conn.commit()
        return True

    except sqlerror:
        print(f"An error occurred while inserting the data. Please Try Again")
        return None


def enter_new_arrivals():
    while True:
        print(f"<<<<< UPDATE BOOK DATA >>>>>")
        id_input = input(f"\nEnter the book id : ")
        table = get_one_book_details(id_input)
        if table:
            print("The <id_input> book Id already exists. Please Try Again")
            print(f"\n{table}")
            return None

        else:
            name = input("Enter the new book name : ")
            author = input("Enter the author name : ")
            price = input("Enter the new price : ")
            catalouge = input("Enter the new calalouge id : ")
            genre = input("Enter the new genre : ")
            print(f"NOTE : Holder is set to <None> for new arrivals")
            new_holder = None
            confirm_input = input(
                f"Are you sure you want to update (Y / N) : ")
            if confirm_input in ['Y', 'y']:
                dl = [id_input, name, author, price,
                      catalouge, genre, new_holder]
                check_var = complete_insert(dl)
                if check_var:
                    print("\nThe data is inserted successfully")
                    new_table = get_one_book_details(id_input)
                    print(f"\n{new_table}")
                    return None

                else:
                    print(f"Couldn't complete the insertion of book. Please Try Again")
                    return None

            else:
                print(f"You chose not to add the book")
                return None
