from tabulate import tabulate
import pymysql

#section - 1

def main():
    print("\n\t\tDOOFENSHMIRTZ EVIL INC.\n")
    print("1. For retriving records, press - 1\n")
    print("2. For reviewing attendance records and/or taking attendance , press - 2\n")
    print("3. To quit, press - 3\n")

    choice = input("Enter valid option:")

    if choice == "1":                             #opens record section
        Rec()
        main()

    elif choice == "2":                           #opens attendance section
        attendanceRec()
        main()

    elif choice == "3":                           #quits
        while True:
            break
    else:
        print("\nERROR! Invalid option entered, please try again.\n\n")
        main()

#section - 2

try:
    from mainFuncs import *
    file = open(r'password.txt', 'r')
    password = file.read()
    file.close
    db = pymysql.connect(host = 'localhost', user = 'root', password = password)    #establishes connection
    c = db.cursor()                               #acivates cursor
    c.execute("use main")
    main()

except:
    print("Please run the setup before running this program.")

