# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Basic Exception Handling and Pickle Demo
# ChangeLog (Who,When,What):
# ISanchez, 11.21.2019, Created Script
# ISanchez, 11.26.2019, Added final edits
# ------------------------------------------------------------------------ #

import pickle
import sys

class BasicMath:
    """ Exception handling examples using simple addition and division"""
    def Addition():
        while True:
            try:
                x = float(input("Please enter the first value: "))
                y = float(input("Please enter the second value: "))
                print("%s plus %s is %s" % (x, y, x + y))
                break
            except ValueError:
                print('Cannot add given values! Please enter numbers only!')
            finally:
                print('Returning to menu')
                break

    def Division():
        while True:
            try:
                x = float(input("Please enter the first value: "))
                y = float(input("Please enter the second value: "))
                print("%s divided by %s is %s" % (x, y, x / y))
                break
            except ValueError:
                print('Cannot divide given values! Please enter numbers only')
            except ZeroDivisionError:
                print('Cannot divide by zero!')
            finally:
                print('Returning to menu')
                break

class Pickle:
    """Demonstrating pickle.dump and pickle.load"""
    def Dump():
        # Saves the dictionary to a pickle file
        numbers = {1, 2, 3, 4, 5}
        strFile = "pickle.txt"
        pickle.dump(numbers, open (strFile, "wb"))
        print(numbers, " dictionary has been pickled to file pickle.txt")
        print('Returning to menu')

    def Load():
        # Loads the dictionary from the pickle file
        try:
            strFile = "pickle.txt"
            numbers = pickle.load(open (strFile, "rb"))
            print("File has been de-pickled! ")
            print(numbers)
        except FileNotFoundError:
            print("File does not exist! Please select option 3 first")
        finally:
            print("Returning to menu")
while True:
    print("""
    Exception Handling and Pickle Demo

    Please select an option:
    1) Addition (Try using letters)
    2) Division (Try to divide by 0)
    3) Create Pickle File
    4) Load Pickle File
    5) Exit Program
    """)
    strChoice = str(input("Please select an option: "))
    if strChoice.strip() == '1':
        BasicMath.Addition()
    elif strChoice.strip() == '2':
        BasicMath.Division()
    elif strChoice.strip() == '3':
        Pickle.Dump()
    elif strChoice.strip() == '4':
        Pickle.Load()
    elif strChoice.strip() == '5':
        break # and exit program
    else:
        print('Please enter a number from the list of options (1-5)')