import pymysql
import time

#section - 1

def connectivity():
    try:
        db = pymysql.connect(host = 'localhost', user = 'root', password = password)    #establishes connection
    except:
        print("\nIvalid password entered, please close and restart the setup.")
    c = db.cursor()
    print("\nLOADING, PLEASE WAIT.")
    try:
        c.execute("CREATE database main")
    except:
        print("\nDatabase main already exists.")
        while True:
            break
    c.execute("use main")
    try:
        c.execute("CREATE TABLE employee(eCode varchar(6) NOT NULL, name varchar(30) NOT NULL, fname varchar(30) NOT NULL, DOA date NOT NULL, DOJPF date NOT NULL, DOJESI date, designation varchar(20), UAN bigint(12) NOT NULL, pfNo varchar(12) NOT NULL, esicNo int(10), gender char(1) NOT NULL, DOB date NOT NULL, MOBno bigint(10) NOT NULL, PANno varchar(11), Aadharno bigint(12) NOT NULL, PRIMARY KEY(eCode, name))")
        c.execute("INSERT INTO employee VALUES('B001', 'Tina Sharma', 'L SH  Shankar Sharma', '1987-10-01', '1994-10-01 ', NULL, 'Director ',  100408378950, 'DL/49620/001', NULL, 'F ', '1967-01-21 ', 9350493139, 'AAFPL1759J ', 823878493572)")
        c.execute("INSERT INTO employee VALUES('B002', 'Tushar Rajawat', 'L SH Piyush Rajawat', '1987-10-01', '1994-10-01', NULL, 'Director', 100333613580, 'DL/49620/002', NULL, 'M', '1968-04-22', 9352496404, 'AABPL1593K', 918323206605)")
        c.execute("INSERT INTO employee VALUES('B003', 'Roohi Sen', 'L SH Narayan Sen', '1994-10-01', '1994-10-01', NULL, 'Accountant', 100276845140, 'DL/49620/003', NULL, 'F', '1969-10-01', 9310048239, 'AAMPL9024A', 652669444822)")
        c.execute("INSERT INTO employee VALUES('B038', 'Inaya Patel', 'SH Rudra Patel', '2008-04-24', '2008-04-24', '2008-04-24', 'Accountant', 100305914277, 'DL/49620/038', 1504715253, 'F', '1966-10-08', 7742517548, 'ANOPY7165N', 310184822295)")
        c.execute("INSERT INTO employee VALUES('B040', 'Siddharth Sachdeva', 'SH Raunak Sachdeva', '2009-12-18', '2009-12-18', '1975-09-15', 'Chief Engineer', 100171869348, 'DL/49620/040', 1505049006, 'M', '1975-09-15', 8502160470, 'BBUPJ8215K', 394182463757)")
        c.execute("INSERT INTO employee VALUES('BECF46', 'Sana Khan', 'SH Firoz Khan', '2012-07-01', '2012-07-01', '2012-07-01', 'Chief Engineer', 100129526953, 'DL/49620/046', 1503962961, 'F', '1985-06-15', 8808067224, 'GBSPK4935M', 890796481835)")
        c.execute("INSERT INTO employee VALUES('BECF47', 'Yash Jain', 'SH Nayan Jain', '2012-07-12', '2012-07-12', '2012-07-12', 'Chief Engineer', 100198152086, 'DL/49620/047', 1506893088, 'M', '1987-08-20', 7688175510, NULL, 439315584672)")
        c.execute("INSERT INTO employee VALUES('BECF48', 'Binod Roy', 'SH Vishesh Roy', '2014-02-01', '2014-02-01', '2019-05-02', 'Assistant Engineer', 116812756447, 'DL/49620/48', '1508792793', 'M', '1968-11-15', 9637910875, 'AUUMPT1579E', 245391548079)")
        c.execute("INSERT INTO employee VALUES('BECF53', 'KD Pathak', 'SH Jagdish Pathak', '2016-12-01', '2016-12-01', '2016-12-01', 'Argon Welder', 100326748946, 'DL/49620/053', 1505060257, 'M',  '1990-07-10', 9784015850, 'DACPR8246B', 800012648639)")
        c.execute("INSERT INTO employee VALUES('BECF54', 'Namit Gupta', 'SH Ram Chandra Gupta', '2017-04-01', '2017-04-01', '2017-04-01', 'Polishman', 101657097172, 'DL/49620/054', 1503762443, 'M', '1980-04-26', 8004626090, 'DXAPP7962P', 954024965463)")
        c.execute("INSERT INTO employee VALUES('BECF60', 'Shipra Mangal', 'L SH Deven Mangal', '2018-08-01', '2018-08-01', '2018-08-01', 'Beta Tester', 104925028350, 'DL/49620/060', 1508268921, 'F', '1977-01-20', 7895188136, 'EEMPB4975C', 435569400892)")
        c.execute("INSERT INTO employee VALUES('BECF55', 'Ranjeet Singh', 'SH Nemi Singh', '2018-03-01', '2018-03-01', '2018-03-01', 'Lath Operator', 101234926696, 'DL/49620/055', 1509451646, 'M', '1988-12-21', '9785631990', NULL, 676293480115)")
        c.execute("INSERT INTO employee VALUES('BECF56', 'Madhav Sharma', 'SH Shiv Sharma', '2018-03-01', '2018-03-01', '2018-03-01', 'Helper', 101267926495, 'DL/49620/056', 1509460425, 'M', '1976-01-01', 8449674851, 'CTGPR7816R', 896782243541)")
        c.execute("INSERT INTO employee VALUES('BECF57', 'Vishram Prajapat', 'SH Lalaram Prajapat', '2018-05-01', '2018-05-01', '2018-05-01', 'Helper', 191001832160, 'DL/49620/057', 1503261628, 'M', '1979-07-15', 9600275313, NULL, 401130193756)")
        c.execute("INSERT INTO employee VALUES('BECF59', 'Harendra Kumar', 'SH Jagdeesh Kumar', '2018-08-01', '2018-08-01', '2018-08-01', 'Helper', 101348064979, 'DL/49620/059', 1509705495, 'M', '1998-07-07', 9116526800, 'HHVPK4005D', 832241746176)")
    except:
        print("\nTable 'employee' and it's data already exists on your device!")
        while True:
            break
    try:
        c.execute("CREATE TABLE attendance(eCode varchar(6) NOT NULL, name varchar(30) NOT NULL, PRIMARY KEY(eCode, name))")
        c.execute("INSERT INTO attendance SELECT eCode, name from employee")    
    except:
        print("\nTable 'attendance' and it's data already exists.")
        while True:
            break
    db.commit()
    print("\nINSTALLATION SUCCESSFUL!!")

#section - 2

passwd = open(r'password.txt', 'w+')
password = input("Enter the MySQL password on your device:")
try:
    passwd.write(password)
    connectivity()
except:
    while True:
        break
passwd.close()


time.sleep(5)
