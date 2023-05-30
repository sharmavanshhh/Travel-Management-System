import random
def rand_num():
    num = random.randint(0,999999)
    return num

import datetime 
def gettime():
    time = datetime.date.today()
    return str(time)

import mysql.connector
con = mysql.connector.connect(user='root',host='localhost', password='va@051206',database='tourist', )

def touristdetails():
    c = con.cursor()
    s = "create table if not exists tourist_det(Tour_ID int,Name char(20),Age int,Contact bigint,Destination varchar(20)," \
        "Address varchar(50),Package varchar(15),Amt_Dept varchar(20) null,Status char(20) null,Book_Date varchar(50))"
    c.execute(s)
    tno = rand_num()
    print("Please Provide Following Details For Further Process -----")
    tname = input('Enter Tourist Name : ')
    age = int(input("Enter Tourist Age : "))
    contact = int(input('Enter Contact Number : '))
    destination = input('Enter Destination : ')
    add = input("Enter Tourist Address : ")
 d   pack = " "
    print('Select the Package : ')
    print(' 1) Rs. 5000/-\n2) Rs. 7000/-\n3) Rs. 10000/-')
    package = int(input('Enter Package : '))
    if package == 1 :
        pack = "Rs. 5000/-"
    elif package == 2 :
        pack = "Rs. 7000/-"
    elif package == 3 :
        pack = "Rs. 10000/-"
    else :
        print("  Oops !! An Error Occured :(\nTry Again !! ")
        touristdetails()
    stt = "Not Confirmed"
    time = gettime()
    data = (tno,tname,age,contact,destination,add,pack,stt,time)
    c = con.cursor()
    qry = "insert into tourist_det(Tour_ID,Name,Age,Contact,Destination,Address,Package,Status,Book_Date) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    c.execute(qry,data)
    con.commit()
    print('Registered Successfully !! ')
    print("Your Tourist ID is - ", tno)
    print("Please Use This ID For Payment Purpose to Confirm Your Booking !! ")
    __main__()

def collectamt():
    tno = input("Enter Tourist ID : ")
    tname = input("Enter Tourist Name : ")
    data = (tno,tname)
    c = con.cursor()
    qry = "select package from tourist_det where Tour_ID=%s and Name=%s"
    c.execute(qry,data)
    d = c.fetchall()
    for i in d :
        pack = 0
        if i[0] == "Rs. 5000/-" :
            pack = 5000
            print("Your Package Costs ~ ", i)
            print("Please Deposit Minimum Rs. 2500/- To Confirm Your Booking")
            amt = int(input("How much amount do you want to deposit ? \n Rs. "))
            if amt < 2500 :
                print("Please Deposit Minimum Rs. 2500/-")
                collectamt()
            elif amt >= 2500 and amt <= pack :
                _amt = "Rs. " + str(amt) + "/-"
                stt = "Confirmed"
                data = (_amt, stt, tno, tname)
                c = con.cursor()
                qry = "update tourist_det set Amt_Dept = %s, Status = %s where Tour_ID = %s and Name = %s"
                c.execute(qry, data)
                con.commit()
                print(" Payment Done !!\n Remaining Amount To Be Paid - Rs. ", pack - amt, "/-")
                print("Booking Confirmed !!")
            elif amt > pack :
                print("You Can Deposit Maximum Rs. 5000/-")
                collectamt()
        elif i[0] == "Rs. 7000/-" :
            pack = 7000
            print("Your Package Costs ~ ", i)
            print("Please Deposit Minimum Rs. 3500/- To Confirm Your Booking")
            amt = int(input("How much amount do you want to deposit ? \n Rs. "))
            if amt < 3500:
                print("Please Deposit Minimum Rs. 3500/-")
                collectamt()
            elif amt >= 3500 and amt <= pack:
                _amt = "Rs. " + str(amt) + "/-"
                stt = "Confirmed"
                data = (_amt,stt,tno,tname)
                c = con.cursor()
                qry = "update tourist_det set Amt_Dept = %s, Status = %s where Tour_ID = %s and Name = %s"
                c.execute(qry, data)
                con.commit()
                print(" Payment Done !!\n Remaining Amount To Be Paid - Rs. ",pack - amt,"/-")
                print(" Booking Confirmed !!")
            elif amt > pack:
                print("You Can Deposit Maximum Rs. 7000/-")
                collectamt()
        elif i[0] == "Rs. 10000/-" :
            pack = 10000
            print("Your Package Costs ~ ", i)
            print("Please Deposit Minimum Rs. 5000/- To Confirm Your Booking")
            amt = int(input("How much amount do you want to deposit ? \n Rs. "))
            if amt < 5000:
                print("Please Deposit Minimum Rs. 5000/-")
                collectamt()
            elif amt >= 5000 and amt <= pack:
                _amt = "Rs. " + str(amt) + "/-"
                stt = "Confirmed"
                data = (_amt, stt, tno, tname)
                c = con.cursor()
                qry = "update tourist_det set Amt_Dept = %s, Status = %s where Tour_ID = %s and Name = %s"
                c.execute(qry, data)
                con.commit()
                print(" Payment Done !!\n Remaining Amount To Be Paid - Rs. ", pack - amt, "/-")
                print(" Booking Confirmed !!")
            elif amt > pack:
                print("You Can Deposit Maximum Rs. 10000/-")
                collectamt()
    __main__()

def searchrecord():
    tno = int(input('Enter Tourist ID : '))
    qry = "(select * from tourist_det where Tour_ID='{}')".format(tno)
    c1 = con.cursor()
    c1.execute(qry)
    rec = c1.fetchall()
    for data in rec :
        print('______________________________________')
        print('Tourist ID : -                             ',data[0])
        print('Tourist Name : -                       ',data[1])
        print('Tourist Age : -                          ',data[2])
        print('Contact No. : -                          ',data[3])
        print('Destination : -                          ',data[4])
        print('Address :-                                ',data[5])
        print('Package :-                                ',data[6])
        print('Amount Deposited : -               ',data[7])
        print('Booking Status : -                    ',data[8])
        print('Booking Date : -                       ',data[9])
        __main__()

def cancelbooking():
    tno = int(input("Enter The Tourist ID For Cancellation: "))
    T = (tno,)
    sql = "Delete from tourist_det where Tour_ID=%s"
    c1 = con.cursor()
    c1.execute(sql,T)
    con.commit()
    print('Cancelled Successfully !!')
    __main__()

def displayall():
    query = "select * from tourist_det"
    c1 = con.cursor()
    c1.execute(query)
    rows = c1.fetchall()
    for data in rows :
        print('______________________________________')
        print('Tourist ID : -                             ', data[0])
        print('Tourist Name : -                       ', data[1])
        print('Tourist Age : -                          ', data[2])
        print('Contact No. : -                          ', data[3])
        print('Destination : -                          ', data[4])
        print('Address :-                                ', data[5])
        print('Package :-                                ', data[6])
        print('Amount Deposited : -               ', data[7])
        print('Booking Status : -                    ', data[8])
        print('Booking Date : -                       ', data[9])
    print('______________________________________')
    print('All records are displayed')
    __main__()

def __main__() :
    print('____________________________________________')
    print("-------Good Luck Tours & Travels-------")
    print('Main Menu')
    print('----------')
    print('1.Add Tourist Record')
    print('2.Deposit Amount')
    print('3.Search Record')
    print('4.Cancel Booking')
    print('5.Display all records ')
    print('6.Exit')
    choice = int(input('Enter your Choice: '))
    if choice == 1:
        touristdetails()
    elif choice == 2:
        collectamt()
    elif choice == 3:
        searchrecord()
    elif choice == 4:
        cancelbooking()
    elif choice == 5:
        displayall()
    elif choice == 6:
        print("Thank You :)")
    else:
        print('Invalid Choice')
        __main__()

__main__()

