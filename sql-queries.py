import mysql.connector as mysql
sql=mysql.connect(host='localhost',user='root',password='Tanishq@2017')
if sql.is_connected():
    print('connected')
else:
    print('not connected')
cr=sql.cursor()
def make():
    cr.execute("create table office(ID int PRIMARY KEY NOT NULL,name varchar(220),gender varchar(220),salary int NOT NULL)")
    sql.commit()
    menu()
cr.execute('use office')
def menu():
    print('*************************')
    print('1: to create table\n2: to add data\n3: to display\n4: to terminate task')
    n=input('enter the desire option to continue: ')
    if n=='1':
        make()
    elif n=='2':
        Input()
    elif n=="3":
        display
    else:
        print("task terminated")
def Input():
    ans='y'
    while ans=='y':
        ID=int(input('enter id number: '))
        name=str(input('enter name: '))
        gender=str(input('enter gender: '))
        salary=input('enter salary: ')
        cr.execute("INSERT INTO employ values ({},'{}','{}',{})".format(ID,name,gender,salary))
        ans=input("enter 'y' if you want to enter more data")
    sql.commit()
    menu()
def display():
    cr.execute('select* from employ')
    r=cr.fetchall()
    print(cr.rowcount)
    for i in r:
        print(i)
    menu()
menu()