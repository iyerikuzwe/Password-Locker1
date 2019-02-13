#!/usr/bin/env python3.6
import random
from user import User
from credentials import Credentials


def create_credential(acc_name, acc_password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(acc_name, acc_password)
    return new_credential


def save_credential(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()


def find_credential(acc_name):
    '''
    Function that finds a credential and returns it
    '''
    return Credentials.find_by_name(acc_name)


def check_existing_credentials(name):
    '''
    Function that check if a credential exists with that name and return a Boolean
    '''
    return Credentials.find_by_name(name)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    while True:
        print("-"*80)
        print("-"*80)
        print("Cool!!Welcome to password_Locker created by Regine Application.")
        print('\n')
        print("The app that saves you from the stress of remembering your passwords for good.")
        print("-"*80)
        print("-"*80)
        print('\n')
        print("Use these short codes to select an option:") 
        print("-"*30)
        print("To create new user account, type: 'cu'")
        print("To log in to your account, type: 'lg'")
        print("To exit password locker, type: 'esc'")
        print("-"*30)
        
        short_code = input().lower()
        print('\n')

        if short_code == 'cu':
            print("Create your preferred username")
            print("-"*29)
            new_username = input()

            print("Create a desired password")
            print("-"*25)
            new_password = input()

            print("Confirm password")
            print("-"*16)
            confirm_password = input()

            while confirm_password != new_password:
                print("Sorry,the inputted passwords did not match! Try again.")
                print("Enter a password")
                new_password = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Woooooh {new_username}! You have created your new account.")
                print("-"*60)
                print('\n')
                print("Proceed to your Account")
                print("-"*24)
                print("Username:")
                created_username = input()
                print("Password:")
                created_password = input()

                while created_username != new_username or created_password != new_password:
                    print("You entered a wrong username or password")
                    print("Username:")
                    created_username = input()
                    print("Your Password")
                    created_password = input()
                    print("-"*24)
                else:
                    print(f"Greetings {created_username}, welcome to your Account")
                    print("Select an option below to continue: Enter either a, b, c, d or e to continue.")
                    print("-"*57)
                    print('\n')

                while True:
                    print("a: View saved account")
                    print("b: Add new account")
                    print("c: Remove existing account")
                    print("d: Search for existing account")
                    print("e: Log Out")
                    print("-"*57)
                    print('\n')
                    option = input()
                    print("-"*50)

                    if option == 'b':
                        while True:
                            print("Continue to add? Type y(for yes)/n(for no)")

                            choice = input().lower()
                            if choice == 'y':
                                print("Enter The Account Name")
                                print("-"*35)
                                acc_name = input()
                                print("Enter a password")
                                print("-"*35)
                                print('\n')
                                print("To generate random password enter keyword 'gen' or 'n' to create your own password")
                                keyword = input().lower()
                                if keyword == 'gen':
                                    acc_password = random.randint(2222222, 22222222)
                                    print(f"Account: {acc_name}")
                                    print(f"Password: {acc_password}")
                                    print('\n')

                                elif keyword == 'n':
                                    print("Create your password")
                                    acc_password = input()
                                    print(f"Account: {acc_name}")
                                    print(f"Password: {acc_password}")
                                    print('\n')

                                else:
                                    print("Please enter a valid Code")

                                save_credential(create_credential(
                                    acc_name, acc_password))
                            elif choice == 'n':
                                break
                            else:
                                print("Please use 'y' for yes or 'n' for no!")
                    elif option == 'a':
                        while True:
                            print("Your registered accounts are as listed as below:")
                            print("-"*40)
                            if display_credentials():

                                for credential in display_credentials():
                                    print(f"ACCOUNT NAME:{credential.acc_name}")
                                    print(f"PASSWORD:{credential.acc_password}")

                            else:
                                print('\n')
                                print("It looks like you do not have any accounts yet")
                                print('\n')

                            print("Return to Main Menu? Type y(for yes)/n(for no)")

                            back = input().lower()
                            if back == 'y':
                                break
                            elif back == 'n':
                                continue
                            else:
                                print("Please Enter a valid code")
                                continue

                    elif option == 'e':
                        print("You will log out of your account. Type y(for yes)/n(for no) to continue...")
                        logout = input().lower()

                        if logout == 'y':
                            print("You have Successfully logged out of your account. Goodbye")
                            break
                        elif logout == 'n':
                            continue
                    elif option == 'c':
                        while True:
                            print("Search for account to delete")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"ACCOUNT NAME: {search_credential.acc_name} \n PASSWORD: {search_credential.acc_password}")
                                print("Delete? y(for yes)/n(for no)")
                                proceed = input().lower()
                                if proceed == 'y':
                                    del_credentials(search_credential)
                                    print("Account deleted")
                                    break
                                elif proceed == 'n':
                                    continue

                            else:
                                print("Contact Does not exist")
                                break

                    elif option == 'd':
                        while True:
                            print("Continue? type y(For yes)/n(For no)")
                            optionb = input().lower()
                            if optionb == 'y':
                                print("Enter an account name")
                                print("-"*20)

                                search_name = input()

                                if check_existing_credentials(search_name):
                                    search_credential = find_credential(
                                        search_name)
                                    print(f"ACCOUNT NAME: {search_credential.acc_name} . PASSWORD: {search_credential.acc_password}")
                                    print("-"*20)
                                else:
                                    print("That Account Does not exist")
                            elif optionb == 'n':
                                break
                            else:
                                print("Please enter a valid code")

                    else:
                        print("Please enter a valid code")
                        continue

        elif short_code == 'lg':
            print("Welcome")
            print("Enter username")
            default_user_name = input()

            print("Enter password")
            default_user_password = input()
            print('\n')

            while default_user_name != 'example' or default_user_password != '23@45':
                print("Wrong username/Password. Default Username is 'example' and password is '23@45'")
                print("Enter Username")
                default_user_name = input()

                print("Enter Your password")
                default_user_password = input()

                print('\n')

            if default_user_name == 'example' and default_user_password == '23@45':
                print("Login Successful!")
                print('\n')
                print("Select an option below to continue: Enter 1, 2, 3, 4 or 5")
                print('\n')

            while True:
                print("1: View saved account")
                print("2: Add new account")
                print("3: Remove account")
                print("4: Search account")
                print("5: Log Out of account")

                option = input()

                if option == '2':
                    while True:
                        print("Continue to add? Type y (for yes)/n (for no)")

                        choice = input().lower()

                        if choice == 'y':
                            print("Enter Account Name")
                            acc_name = input()
                            print("Enter a password")
                            print("To generate random password enter keyword 'gp' or 'n' to create your own password")
                            keyword = input().lower()
                            if keyword == 'gp':
                                acc_password = random.randint(222222, 2222222)
                                print(f"Account: {acc_name}")
                                print(f"Password: {acc_password}")
                                print('\n')
                            elif keyword == 'n':
                                print("Create your password")
                                acc_password = input()
                                print(f"Account: {acc_name}")
                                print(f"Password: {acc_password}")
                                print('\n')

                            else:
                                print("Please enter a valid Code")

                            save_credential(create_credential(acc_name, acc_password))
                        elif choice == 'n':
                            break
                        else:
                            print("Please use 'y' for yes or 'n' for no!")
                elif option == '1':
                    while True:
                        print("Listed below are all your accounts")
                        if display_credentials():

                            for credential in display_credentials():
                                print(f"ACCOUNT NAME:{credential.acc_name}")
                                print(f"PASSWORD:{credential.acc_password}")

                        else:
                            print('\n')
                            print("You don't seem to have any contacts yet")
                            print('\n')

                        print("Back to Main Menu? y(For yes)/n(For no)")

                        back = input().lower()
                        if back == 'y':
                            break
                        elif back == 'n':
                            continue
                        else:
                            print("Please Enter a valid code")
                elif option == '5':
                    print("You will be logged out of your account. Are you sure? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print("You have Successfully logged out")
                        break
                    elif logout == 'n':
                        continue

                elif option == '3':
                    while True:
                        print("Search for credential to delete")

                        search_name = input()

                        if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(f"ACCOUNT NAME: {search_credential.acc_name} \n PASSWORD: {search_credential.acc_password}")
                            print("Delete? y/n")
                            sure = input().lower()
                            if sure == 'y':
                                del_credentials(search_credential)
                                print("Account deleted")
                                break
                            elif sure == 'n':
                                continue

                        else:
                            print("That account Does not exist")
                            break

                elif option == '4':
                    while True:
                        print("Continue? y/n")
                        option2 = input().lower()
                        if option2 == 'y':
                            print("Enter an account name")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(
                                    search_name)
                                print(f"ACCOUNT NAME: {search_credential.acc_name} \n PASSWORD: {search_credential.acc_password}")
                            else:
                                print("That Contact Does not exist")
                        elif option2 == 'n':
                            break
                        else:
                            print("Please enter a valid code")
                else:
                    print("Please enter a valid code")
        elif short_code == 'esc':
            break
        else:
            print("Please Enter a valid code to continue")


if __name__ == '__main__':
    main()


