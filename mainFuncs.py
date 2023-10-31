from tabulate import tabulate
import pymysql

#section - 1

file = open(r'password.txt', 'r')
password = file.read()
file.close
try:
    db = pymysql.connect(host = 'localhost', user = 'root', password = password)    #establishes connection
    c = db.cursor()                               #acivates cursor
    c.execute("use main")
except:
    print("\n")

#section - 2

def showAllRec():                             #fetches records of all
    c.execute("select * from employee")
    rows = c.fetchall()
    data = [["ECode", "Name", "Father's Name", "DOA", "DOJ PF", "DOJ ESI", "Designation", "UAN", "PF no", "ESIC no", "Gender", "DOB", "MOB no", "PAN no", "Aadhar no"]]
    for tup in rows:
        lst = list(tup)
        data.append(lst)
    print(tabulate(data))

def singleRecviaEcode():
    eCode = input("\nEnter Employee Code:")                             #takes employee code
    c.execute("Select * from employee WHERE eCode = '"+eCode.upper()+"'")
    row = c.fetchmany(1)
    data = [["ECode", "Name", "Father's Name", "DOA", "DOJ PF", "DOJ ESI", "Designation", "UAN", "PF no", "ESIC no", "Gender", "DOB", "MOB no", "PAN no", "Aadhar no"]]
    while row:                                                          #parses row
        for tup in row:
            lst = list(tup)                                             #converts tuple to list
            data.append(lst)                                            #adds data to dislay table 
        print(tabulate(data))
        break
    else:                                                               #error statement
        print("\nNo employee with Employee Code",eCode,"found.")
        print("\n")
        singleRecviaEcode()

def singleRecviaName():
    name = input("\nEnter name of employee:")                           #takes name of employee
    c.execute("Select * from employee WHERE name LIKE '%"+name.capitalize()+"%'")
    row = c.fetchmany(1)
    data = [["ECode", "Name", "Father's Name", "DOA", "DOJ PF", "DOJ ESI", "Designation", "UAN", "PF no", "ESIC no", "Gender", "DOB", "MOB no", "PAN no", "Aadhar no"]]
    while row:                                                          #parses row
        for tup in row:
            lst = list(tup)                                             #converts tuple to list
            data.append(lst)                                            #adds data to dislay table 
        print(tabulate(data))
        break
    else:                                                               #error statement
        print("\nNo employee named",name,"found.")
        print("\n")
        singleRecviaName()

def singleRecviaMobNo():
    mob = input("\nEnter employee's mobile number:")                    #takes mobile number of employee
    c.execute("Select * from employee where MOBno = "+mob+"")
    row = c.fetchmany(1)
    data = [["ECode", "Name", "Father's Name", "DOA", "DOJ PF", "DOJ ESI", "Designation", "UAN", "PF no", "ESIC no", "Gender", "DOB", "MOB no", "PAN no", "Aadhar no"]]
    while row:                                                          #parses row
        for tup in row:
            lst = list(tup)                                             #converts tuple to list
            data.append(lst)                                            #adds data to dislay table 
        print(tabulate(data))
        break
    else:                                                               #error statement
        print("\nNo employe with mobile number",mob,"found.")
        singleRecviaMobNo()

def singleRecviaPANno():
    pan_no = input("\nEnter employee's PAN number:")                    #takes PAN number of employee
    c.execute("SELECT * from employee WHERE PANno = '"+pan_no.upper().strip()+"'")
    row = c.fetchmany(1)
    data = [["ECode", "Name", "Father's Name", "DOA", "DOJ PF", "DOJ ESI", "Designation", "UAN", "PF no", "ESIC no", "Gender", "DOB", "MOB no", "PAN no", "Aadhar no"]]
    while row:                                                          #parses row
        for tup in row:
            lst = list(tup)                                             #converts tuple to list
            data.append(lst)                                            #adds data to dislay table 
        print(tabulate(data))
        break
    else:                                                               #error statement
        print("\nNo employee with PAN no",pan_no,"found.")
        singleRecviaPANno()

def singleRecviaAadhar():
    a_no = input("\nEnter employee's Aadhar number:")                   #takes Aadhar number of employee
    c.execute("Select * from employee WHERE Aadharno = "+a_no+"")
    row = c.fetchmany(1)
    data = [["ECode", "Name", "Father's Name", "DOA", "DOJ PF", "DOJ ESI", "Designation", "UAN", "PF no", "ESIC no", "Gender", "DOB", "MOB no", "PAN no", "Aadhar no"]]
    while row:                                                          #parses row
        for tup in row:
            lst = list(tup)                                             #converts tuple to list
            data.append(lst)                                            #adds data to dislay table 
        print(tabulate(data))
        break
    else:                                                               #error statement
        print("\nNo employee with Aadhar number",a_no,"found.")
        print("\n")
        singleRecviaAadhar()

def Rec():
    print("\n\t\t\tEMPLOYEE DATA\n")
    print("1. For retriving information of all employees, press - 1\n")
    print("2. For retriving information based on employee's code, press - 2\n")
    print("3. For retriving information based on Na2me, press - 3\n")
    print("4. For retriving information based on mobile number, press - 4\n")
    print("5. For retriving information based on Pan number, press - 5\n")
    print("6. For retriving information based on Aadhar number, press - 6\n")

    info = input("Enter valid option:")

    if info == "1":
        print("\n\t\t\t\t\t\tEMPLOYEE INFO\n")
        showAllRec()

    elif info == "2":
        singleRecviaEcode()

    elif info == "3":
        singleRecviaName()

    elif info == "4":
        singleRecviaMobNo()

    elif info == "5":
        singleRecviaPANno()

    elif info == "6":
        singleRecviaAadhar()
    else:
        print("Invalid entry, please try again.\n")

#section - 3

def attendance():
    c.execute("select eCode, name from attendance ORDER BY name")
    rows = c.fetchall()
    date = input("Enter the date(DDMMMMYY):")                                     #takes current date
    print("\n")
    try:
        c.execute("ALTER TABLE attendance ADD "+date+" char(2) NOT NULL")   #creates new column of input date
        db.commit()
        for r in rows:
            print(r, end = '')
            status = input(":") #takes attendance status (present, absent, casual leave, economic leave, sick leave)
            print('\n')
            if status.upper() == "P":
                c.execute("UPDATE attendance SET "+date+" ='P' WHERE eCode = '"+r[0]+"'")   #updates status present
                db.commit()
            elif status.upper() == "A":
                c.execute("UPDATE attendance SET "+date+" ='A' WHERE eCode = '"+r[0]+"'")   #updates status absent
                db.commit()
            elif status.upper() == "CL":
                c.execute("UPDATE attendance SET "+date+" ='CL' WHERE eCode = '"+r[0]+"'")  #updates status casual leave
                db.commit()
            elif status.upper() == "EL":
                c.execute("UPDATE attendance SET "+date+" ='EL' WHERE eCode = '"+r[0]+"'")  #updates status paid leave
                db.commit()
            elif status.upper() == "SL":
                c.execute("UPDATE attendance SET "+date+" ='SL' WHERE eCode = '"+r[0]+"'")  #updates status sick leave
                db.commit()
            else:
                print("\nERROR! Invalid Entry, please start over.\n")
                c.execute("Alter table attendance drop "+date+"")
                db.commit()
                attendance()
    except:
        print("The attendance of",date,"already exists.")
        attendance()

def retriveAttendanceDate():
    date = input("Enter date in dd(month)yy format:")
    print("\n")
    try:
        data1 = ['', '']
        data1.append(date)
        c.execute("Select eCode, name, "+date+" from attendance ORDER BY name")
        row = c.fetchall()
        data = []
        data.append(data1)
        for tup in row:
            lst = list(tup)
            data.append(lst)
        print(tabulate(data))
    except:
        print("Invalid date entered, please try again.")

def deleteAttendanceRecDate():
    date = input("Enter date in dd(month)yy format:")
    try:
        c.execute("Alter table attendance drop "+date+"")
        db.commit()
        print("\nRecord successfully deleted.\n")
    except:
        print("\nInvalid date entered, please enter again.\n")
        deleteAttendanceRecDate()

def attendanceRec():
    print("\n\t\tATTENDANCE\n")
    print("1. For taking attendance, press - 1\n")
    print("2. For reviewing attendance(daily), press - 2\n")
    print("3. For delete attendance record, press - 3\n")

    choice = input("Enter valid option:")
    print("\n")
    if choice == "1":
        attendance()

    elif choice == "2":
        retriveAttendanceDate()

    elif choice == "3":
        deleteAttendanceRecDate()

