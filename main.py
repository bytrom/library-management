import mysql.connector as sq
from mysql.connector import Error as sqlerror
from os import system
import src
from getpass import getpass
from random import randint


def answer_question(username):
    q_list = ['This is question 1', 'This is question 2', 'This is question 3']
    a_list = ['Answer 1', 'Answer 2', 'Answer 3']
    points = 0

    for i in range(len(q_list)):
        q = q_list[i]
        a = a_list[i]

        print(f"Question {i}:{q}")
        answer_input = input(f"Enter your answer : ")

        if answer_input == a:
            points += 1

        else:
            continue

    if points >= 2:
        print(f"You are authorized")
        src.change_password(username)


main_menu = """<<<<< MAIN MENU >>>>>
---------------------------------------------------
♻    1.Display Available Books               ♻
♻    2.Display Available Magazines           ♻
♻    3.Update the book Details               ♻
♻    4.Enter new Arrivals                    ♻
♻    5.Change your Password                  ♻
♻    6.To Quit                               ♻
---------------------------------------------------"""

heading = """<<<<<    Welcome to Library   >>>>>
------ Sainik School Kalikiri ------\n"""

system('cls')
print(heading)

menu_dict = {'1': src.show_book_table,
             '2': src.show_magazine_table,
             '3': src.update_book_details,
             '4': src.enter_new_arrivals,
             '5': src.validate_change_password,
             '6': src.quit_program}


def show_menu():
    while True:
        print(main_menu)
        option_input = input("Enter your option : ")

        if option_input in menu_dict:
            menu_dict[option_input]()

        else:
            print(
                f"\n<{option_input}> is an invalid input. Please Try Again")
            continue


while True:

    username_input = input("Enter your username : ")
    conn, cursor = src.establish_conn()
    cursor.execute(
        f"SELECT name, password from users WHERE username = '{username_input}'")
    data = cursor.fetchone()
    conn.close()
    if not data:
        print(f"You have entered an invalid username. Please try again")
        continue

    else:
        password_input = getpass("Enter your password : ")
        if password_input == data[1]:
            print("\nAccess Granted")
            show_menu()

        else:
            print(
                f"\nYou have entered an invalid password.To get access please answer the security question")
            answer_question(username_input)
