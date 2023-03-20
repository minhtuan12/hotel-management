# Functions
import decimal
import getpass as w
import time
import os
import mysql.connector as mycon


def colorText(text):
    COLORS = {
        "black": "\u001b[30;1m",
        "red": "\u001b[31;1m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33;1m",
        "blue": "\u001b[34;1m",
        "magenta": "\u001b[35m",
        "cyan": "\u001b[36m",
        "white": "\u001b[37m",
        "yellow-background": "\u001b[43m",
        "black-background": "\u001b[40m",
        "cyan-background": "\u001b[46;1m",
    }
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


# Main Program


os.system("cls")
a = ("""
\t\t\t\t[[yellow]]|= = = = = = = = = = = = = = = = = = = = = = = = = = = =|
\t\t\t\t[[green]]|*******************************************************|
\t\t\t\t|[[cyan]]\t\tWELCOME TO Grandeur Resort\t\t[[green]]|
\t\t\t\t[[green]]|*******************************************************|
\t\t\t\t[[yellow]]|= = = = = = = = = = = = = = = = = = = = = = = = = = = =|
[[white]]""")


def start(t):
    os.system('cls')
    col, row = os.get_terminal_size()
    row = row-1

    t1 = "connecting to MAIN servers"
    t2 = "logging in to MAIN servers"
    dot = '.'*int((col-10-len(t)-len(t1)-len(t2))/4)
    s = '|#'+dot + t1 + dot+'#| '+t+' |#'+dot + t2 + dot+'#|'
    l = len(s)

    a1 = r"     _____     "
    a2 = r"  __/__|__\__  "
    a3 = r" /  _ +++ _  \ "
    a4 = r"'--(_)---(_)--'"

    w1 = r'__      _____ _    ___ ___  __  __ ___ '
    w2 = r'\ \    / / __| |  / __/ _ \|  \/  | __|'
    w3 = r' \ \/\/ /| _|| |_| (_| (_) | |\/| | _| '
    w4 = r'  \_/\_/ |___|____\___\___/|_|  |_|___|'

    sp = ' '*int((l-len(a4)-len(w3))/2)
    w1 = sp+w1+sp
    w2 = sp+w2+sp
    w3 = sp+w3+sp
    w4 = sp+w4+sp

    n = int((row-9)/2)-1
    for y in range(0, l+1):
        os.system('cls')
        for x in range(n):
            print(s[:y])
        print("")
        print("")
        print(w1[0:y]+a1)
        print(w2[0:y]+a2)
        print(w3[0:y]+a3)
        print(w4[0:y]+a4)
        print("="*l)
        print("")
        print("")
        for x in range(n):
            print(s[:y])
        time.sleep(0.000000000000000000001)
    input('')
    os.system('cls')
    return


start("Grandeur Resort")
while True:
    os.system('cls')
    print(colorText(
        "\n\n\n\t\tEnter your computer's MY_SQL [[magenta]]Password[[white]] : "), end="")
    pw = w.getpass('')
    os.system('cls')
    try:
        cn = mycon.connect(host='localhost', user='root',
                           passwd=pw, database='hotel_management2')
    except:
        print(
            colorText('\n\t\t[[green]]Connection Failed...[[white]]\nEnter Again... '))
        time.sleep(1)
        continue
    break
mycur = cn.cursor()
os.system('cls')

b = ("""[[cyan]]1. [[yellow]]Enter Customer Data and Room Rent[[cyan]]
2. [[yellow]]Calculate Laundry bill[[cyan]]
3. [[yellow]]Calculate Restaurant bill[[cyan]]
4. [[yellow]]Calculate Game bill[[cyan]]
5. [[yellow]]Calculate Bar bill[[cyan]]
6. [[yellow]]Calculate Amusement activity bill[[cyan]]
7. [[yellow]]Calculate Car Rental bill[[cyan]]
8. [[yellow]]Calculate Spa and Extra services bill[[cyan]]
9. [[yellow]]Show Total Revenue Generated[[cyan]]
10. [[yellow]]To Generate Bill[[cyan]]
0. [[yellow]]EXIT[[white]]\n\n""")
print(colorText(a))

print(colorText(
    """\t\t[[blue]]1][[white]] ADMIN\n\t\t[[red]]2][[white]] RECEPTION\n\t\t[[blue]]3][[white]] EXIT"""))
ch1 = int(input("Enter the Choice: "))
os.system("cls")
ch = -1

cust = []


def check(t):
    if t == (0,):
        print(colorText('[[green]]Empty![[white]]'))
    else:
        print(colorText('[[red]]Used![[white]]'))


while ch1 != 3:

    if ch1 == 2:
        # For Reception
        os.system("cls")
        print(colorText(a))
        print(colorText(b))
        ch = int(input("Enter the Choice: "))
        s = 0
        while ch != 0:
            if ch == 1:
                mycur.execute("SELECT status_room FROM statuss")
                data = mycur.fetchall()
                print("\nWe have the following rooms for you:-")
                print("1.  Room number 101: 6000", end=' ----- ')
                check(data[0])
                print("2.  Room number 102: 5000", end=' ----- ')
                check(data[1])
                print("3.  Room number 103: 4000", end=' ----- ')
                check(data[2])
                print("4.  Room number 104: 3000", end=' ----- ')
                check(data[3])

                mycur.execute("SELECT Room_no FROM cust_data")
                data = mycur.fetchall()
                ro = [101, 102, 103, 104]
                rno = int(input("Enter the room number: "))
                tmp = (rno,)
                while True:
                    if tmp in data or rno not in ro:
                        print(colorText(
                            "[[red]]This room number has been already booked or not exists![[white]]"))
                        rno = int(input("Enter the room number: "))
                        tmp = (rno,)
                    else:
                        break

                mycur.execute(
                    "UPDATE statuss SET status_room = {0} WHERE Room_no = {1}".format(1, rno))
                cn.commit()
                n = input("Enter the name: ")
                add = input("Enter the address: ")
                no = int(input("Enter the number of days: "))

                if rno == 101:
                    s = no*6000
                    q = "insert into Cust_data values('{0}','{1}','{2}','{3}','{4}','{5}')".format(
                        rno, n, add, no, 'A', s)
                    mycur.execute(q)
                    cn.commit()
                elif rno == 102:
                    s = no*5000
                    q = "insert into Cust_data values('{0}','{1}','{2}','{3}','{4}','{5}')".format(
                        rno, n, add, no, 'B', s)
                    mycur.execute(q)
                    cn.commit()
                elif rno == 103:
                    s = no*4000
                    q = "insert into Cust_data values('{0}','{1}','{2}','{3}','{4}','{5}')".format(
                        rno, n, add, no, 'C', s)
                    mycur.execute(q)
                    cn.commit()
                elif rno == 104:
                    s = no*3000
                    q = "insert into Cust_data values('{0}','{1}','{2}','{3}','{4}','{5}')".format(
                        rno, n, add, no, 'D', s)
                    mycur.execute(q)
                    cn.commit()

                my = cn.cursor()
                qq = "insert into Laundry_bill(Room_No) values('{0}')".format(
                    rno)
                my.execute(qq)
                qq = "insert into Bar_bill(Room_No) values('{0}')".format(rno)
                my.execute(qq)
                qq = "insert into Food_bill(Room_No) values('{0}')".format(rno)
                my.execute(qq)
                qq = "insert into Amusement_bill(Room_No) values('{0}')".format(
                    rno)
                my.execute(qq)
                qq = "insert into Services_bill(Room_No) values('{0}')".format(
                    rno)
                my.execute(qq)
                qq = "insert into Game_bill(Room_No) values('{0}')".format(rno)
                my.execute(qq)
                qq = "insert into Carrent_bill(Room_No) values('{0}')".format(
                    rno)
                my.execute(qq)
                cn.commit()
                ex = input(
                    colorText("Press [[green]]ENTER[[white]] to return"))
                os.system('cls')
                print(colorText(a))
                print(colorText(b))
                ch = int(input("Enter the Choice: "))
            elif ch == 3:
                # Restro
                mycur2 = cn.cursor()
                rno = int(input("Enter the room number: "))
                print("\n\t\t*****RESTAURANT MENU*****")
                print(" 1. Water----->Rs20\n",
                      "2. Tea----->Rs10\n",
                      "3. Breakfast Combo--->Rs90\n",
                      "4. Lunch Combo---->Rs110\n",
                      "5. Dinner Combo--->Rs150\n",
                      "6. Exit")

                x = 0

                sr = 0
                while x != 6:
                    x = int(input("Enter the Order: "))
                    if x == 1:
                        n = int(input("\tEnter the quantity: "))
                        A = 'Water'
                        sr = sr+n*20
                        q = "Update Food_bill set Num_water='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur2.execute(q)
                    elif x == 2:
                        n = int(input("\tEnter the quantity: "))
                        q = "Update Food_bill set Num_tea='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'Tea'
                        sr = sr+n*10
                        mycur2.execute(q)
                    elif x == 3:
                        n = int(input("\tEnter the quantity: "))
                        q = "Update Food_bill set Num_breakfastcombo='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'Breakfast Combo'
                        sr = sr+n*90
                        mycur2.execute(q)
                    elif x == 4:
                        n = int(input("\tEnter the quantity: "))
                        q = "Update Food_bill set Num_lunchcombo='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'Lunch'
                        sr = sr+n*110
                        mycur2.execute(q)
                    elif x == 5:
                        n = int(input("\tEnter the quantity: "))
                        q = "Update Food_bill set Num_dinnercombo='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'Dinner'
                        sr = sr+n*150
                        mycur2.execute(q)
                print(colorText(
                    "[[yellow-background]]---------->Your Restaurant Bill is:[[black-background]] "), sr)
                q = "Update Food_bill set Food_bill='{0}' where room_no='{1}'".format(
                    sr, rno)
                mycur2.execute(q)
                cn.commit()
                ex = input(
                    colorText("Press [[green]]ENTER[[white]] to return"))
                os.system('cls')
                print(colorText(a))
                print(colorText(b))
                ch = int(input("Enter the Choice: "))
            elif ch == 2:
                # Laundry
                mycur3 = cn.cursor()
                rno = int(input("Enter the Room number: "))
                print("\n\t\t******LAUNDRY MENU*******")
                print(" 1. Shorts----->Rs3\n",
                      "2. Trousers----->Rs4\n",
                      "3. Shirt--->Rs5\n",
                      "4. Jeans---->Rs6\n",
                      "5. Girlsuit--->Rs8\n",
                      "6. Exit")

                x = 0
                sl = 0
                while x != 6:
                    x = int(input("Enter the Option: "))
                    if x == 1:
                        n = int(input("\tEnter the quantity: "))
                        A = 'Shorts'
                        q = "Update Laundry_bill set Num_Shorts='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur3.execute(q)
                        sl = sl+n*3
                    elif x == 2:
                        n = int(input("\tEnter the quantity: "))
                        A = 'Trousers'
                        q = "Update Laundry_bill set Num_Trousers='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur3.execute(q)
                        sl = sl+n*4
                    elif x == 3:
                        n = int(input("\tEnter the quantity: "))
                        A = 'Shirt'
                        q = "Update Laundry_bill set Num_Shirt='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur3.execute(q)
                        sl = sl+n*5
                    elif x == 4:
                        n = int(input("\tEnter the quantity: "))
                        A = 'Jeans'
                        q = "Update Laundry_bill set Num_Jeans='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur3.execute(q)
                        sl = sl+n*6
                    elif x == 5:
                        n = int(input("\tEnter the quantity: "))
                        q = "Update Laundry_bill set Num_Girlsuit='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur3.execute(q)
                        A = 'Girlsuit'
                        sl = sl+n*8
                print(colorText(
                    "[[yellow-background]]---------->Your Laundry Bill is:[[black-background]] "), sl)
                q = "Update Laundry_bill set Laundry_bill='{0}' where room_no='{1}'".format(
                    sl, rno)
                mycur3.execute(q)
                cn.commit()
                ex = input(
                    colorText("Press [[green]]ENTER[[white]] to return"))
                os.system('cls')
                print(colorText(b))
                ch = int(input("Enter the Choice: "))
            elif ch == 4:
                # Game
                rno = int(input("Enter the Room number: "))
                print("\n\t\t******GAME MENU*******")
                print(" 1. Table tennis----->Rs60\n",
                      "2. Bowling----->Rs80\n",
                      "3. Snooker--->Rs70\n",
                      "4. Video games---->Rs90\n",
                      "5. Pool--->Rs50\n",
                      "6. Exit")
                mycur4 = cn.cursor()

                x = 0
                sg = 0
                while x != 6:
                    x = int(input("Enter the Opt: "))
                    if x == 1:
                        n = int(input("\tEnter no. of hours: "))
                        q = "Update Game_bill set Num_tabletennis='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur4.execute(q)
                        A = 'Table Tennis'
                        sg = sg+n*60
                    elif x == 2:
                        n = int(input("\tEnter no. of hours: "))
                        q = "Update Game_bill set Num_bowling='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur4.execute(q)
                        A = 'Bowling'
                        sg = sg+n*80
                    elif x == 3:
                        n = int(input("\tEnter no. of hours: "))
                        q = "Update Game_bill set Num_snooker='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur4.execute(q)
                        A = 'Snooker'
                        sg = sg+n*70
                    elif x == 4:
                        n = int(input("\tEnter no. of hours: "))
                        A = 'Video Games'
                        q = "Update Game_bill set Num_videogames='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur4.execute(q)
                        sg = sg+n*90
                    elif x == 5:
                        n = int(input("\tEnter no. of hours: "))
                        A = 'Pool'
                        q = "Update Game_bill set Num_Pool='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur4.execute(q)
                        sg = sg+n*50
                print(colorText(
                    "[[yellow-background]]---------->Your Gaming Bill is:[[black-background]] "), sg)
                q = "Update Game_bill set game_bill='{0}' where room_no='{1}'".format(
                    sg, rno)
                mycur4.execute(q)
                cn.commit()
                ex = input(
                    colorText("Press [[green]]ENTER[[white]] to return"))
                os.system('cls')
                print(colorText(a))
                print(colorText(b))
                ch = int(input("Enter the Choice: "))
            elif ch == 5:
                # Bar
                mycur5 = cn.cursor()
                rno = int(input("Enter the room number: "))
                print("\n\t\t*****BAR MENU*****")
                print(" 1. Water----->Rs20\n",
                      "2. Pinacolada----->Rs120\n",
                      "3. Fruit Punch--->Rs110\n",
                      "4. Scotch Whiskey---->Rs180\n",
                      "5. Vodka Shots--->Rs200\n",
                      "6. Exit")
                x = 0

                sr = 0
                while x != 6:
                    x = int(input("Enter the Order: "))
                    if x == 1:
                        n = int(input("\tEnter the quantity: "))
                        A = 'Water'
                        sr = sr+n*20
                        q = "Update bar_bill set Num_water='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur5.execute(q)
                    elif x == 2:
                        n = int(input("\tEnter the quantity: "))
                        q = "Update bar_bill set Num_pinacolada='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'pinacolada'
                        sr = sr+n*120
                        mycur5.execute(q)
                    elif x == 3:
                        n = int(input("\tEnter the quantity: "))
                        q = "Update bar_bill set Num_Fruitpunch='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'fruitpunch'
                        sr = sr+n*110
                        mycur5.execute(q)
                    elif x == 4:
                        n = int(input("\tEnter the quantity: "))
                        q = "Update bar_bill set Num_Scotchwhiskey='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'Scotchwhiskey'
                        sr = sr+n*180
                        mycur5.execute(q)
                    elif x == 5:
                        n = int(input("\tEnter the quantity: "))
                        q = "Update bar_bill set Num_vodkashots='{0}'".format(
                            n, rno)
                        A = 'Vodkashots'
                        sr = sr+n*200
                        mycur5.execute(q)
                print(colorText(
                    "[[yellow-background]]---------->Your Bar Bill is:[[black-background]] "), sr)
                q = "Update bar_bill set bar_bill='{0}' where room_no='{1}'".format(
                    sr, rno)
                mycur5.execute(q)
                cn.commit()
                ex = input(
                    colorText("Press [[green]]ENTER[[white]] to return"))
                os.system('cls')
                print(colorText(a))
                print(colorText(b))
                ch = int(input("Enter the Choice: "))
            elif ch == 6:
                # Amusement Activity
                mycur6 = cn.cursor()
                rno = int(input("Enter the room number: "))
                print("\n\t\t*****AMUSEMENT ACTIVITIES*****")
                print(" 1. Water Polo--->Rs400\n",
                      "2. Bumping Cars--->Rs120\n",
                      "3. 4D Movie--->Rs140\n",
                      "4. Go Kart Racing--->Rs640\n",
                      "5. F1 Simulator--->Rs290\n",
                      "6. Exit")

                x = 0

                sr = 0
                while x != 6:
                    x = int(input("Enter the Option: "))
                    if x == 1:
                        n = int(input("\tEnter the quantity: "))
                        A = 'WaterPOLO'
                        sr = sr+n*400
                        q = "Update amusement_bill set Num_Waterpolo='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur6.execute(q)
                    elif x == 2:
                        n = int(input("\tEnter the quantity: "))
                        q = "Update amusement_bill set Num_Bumpingcar='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'BumpingCARS'
                        sr = sr+n*120
                        mycur6.execute(q)
                    elif x == 3:
                        n = int(input("\tEnter the No. of tickets: "))
                        q = "Update amusement_bill set Num_4DMovie='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = '4D Movie'
                        sr = sr+n*140
                        mycur6.execute(q)
                    elif x == 4:
                        n = int(input("\tEnter the No. of tickets: "))
                        q = "Update amusement_bill set Num_GoKart='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'GoKart'
                        sr = sr+n*640
                        mycur6.execute(q)
                    elif x == 5:
                        n = int(input("\tEnter the quantity: "))
                        q = "Update amusement_bill set Num_F1Sim='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'F1 Simulator'
                        sr = sr+n*290
                        mycur6.execute(q)
                print(colorText(
                    "[[yellow-background]]---------->Your Amusement Activity Bill is:[[black-background]] "), sr)
                q = "Update amusement_bill set amusement_bill='{0}' where room_no='{1}'".format(
                    sr, rno)
                mycur6.execute(q)
                cn.commit()
                ex = input(
                    colorText("Press [[green]]ENTER[[white]] to return"))
                os.system('cls')
                print(colorText(a))
                print(colorText(b))
                ch = int(input("Enter the Choice: "))
            elif ch == 7:
                # Car Rental
                mycur7 = cn.cursor()
                rno = int(input("Enter the room number: "))
                print("\n\t\t*****CAR TYPES FOR Sight-Seeing*****")
                print(" 1. Jeep Cherokee--->Rs7.9k\n",
                      "2. Land Rover Defender--->Rs8.1k\n",
                      "3. Volkswagen Van--->Rs6.0k\n",
                      "4. Mercedes G Wagen--->Rs9.2k\n",
                      "5. Rolls Royce Ghost--->Rs12.0k\n",
                      "6. Exit")
                x = 0

                sr = 0
                while x != 6:
                    x = int(input("Enter the Order: "))
                    if x == 1:
                        n = int(input("\tEnter No. of days: "))
                        A = 'Jeep'
                        sr = sr+n*7900
                        q = "Update CarRent_bill set Num_Jeep='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur7.execute(q)
                    elif x == 2:
                        n = int(input("\tEnter No. of days: "))
                        q = "Update CarRent_bill set Num_landrover='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'Land Rover'
                        sr = sr+n*8100
                        mycur7.execute(q)
                    elif x == 3:
                        n = int(input("\tEnter No. of days: "))
                        q = "Update CarRent_bill set Num_Volkswagen='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'Volkswagen'
                        sr = sr+n*6000
                        mycur7.execute(q)
                    elif x == 4:
                        n = int(input("\tEnter No. of days: "))
                        q = "Update CarRent_bill set Num_Mercedes='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'Mercedes'
                        sr = sr+n*9200
                        mycur7.execute(q)
                    elif x == 5:
                        n = int(input("\tEnter No. of days: "))
                        q = "Update CarRent_bill set Num_rollsroyce='{0}'".format(
                            n, rno)
                        A = 'Rolls Royce'
                        sr = sr+n*12000
                        mycur7.execute(q)
                print(colorText(
                    "[[yellow-background]]---------->Your CarRental Bill is:[[black-background]] "), sr)
                q = "Update CarRent_bill set CarRent_bill='{0}' where room_no='{1}'".format(
                    sr, rno)
                mycur7.execute(q)
                cn.commit()
                ex = input(
                    colorText("Press [[green]]ENTER[[white]] to return"))
                os.system('cls')
                print(colorText(a))
                print(colorText(b))
                ch = int(input("Enter the Choice: "))
            elif ch == 8:
                # Services
                mycur8 = cn.cursor()
                rno = int(input("Enter the room number: "))
                print("\n\t\t*****Special Services*****")
                print(" 1. Hair Spa--->Rs1.0k\n",
                      "2. Body Spa--->Rs2.2k\n",
                      "3. Hot Waterbath--->Rs1.0k\n",
                      "4. Outdoor Gym--->Rs700\n",
                      "5. Indoor Gym--->Rs680\n",
                      "6. Exit")

                x = 0

                sr = 0
                while x != 6:
                    x = int(input("Enter the Option: "))
                    if x == 1:
                        n = int(input("\tEnter No. of people: "))
                        A = 'Hair Spa'
                        sr = sr+n*1000
                        q = "Update Services_bill set Num_hairspa='{0}' where room_no='{1}'".format(
                            n, rno)
                        mycur8.execute(q)
                    elif x == 2:
                        n = int(input("\tEnter No. of people: "))
                        q = "Update Services_bill set Num_bodyspa='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'Body Spa'
                        sr = sr+n*2200
                        mycur8.execute(q)
                    elif x == 3:
                        n = int(input("\tEnter No. of Hours: "))
                        q = "Update Services_bill set Num_hotwaterbath='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'Hot Waterbath'
                        sr = sr+n*1000
                        mycur8.execute(q)
                    elif x == 4:
                        n = int(input("\tEnter No. of Hours: "))
                        q = "Update Services_bill set Num_Indoorgym='{0}' where room_no='{1}'".format(
                            n, rno)
                        A = 'Indoor Gym'
                        sr = sr+n*700
                        mycur8.execute(q)
                    elif x == 5:
                        n = int(input("\tEnter No. of Hours: "))
                        q = "Update Services_bill set Num_Outdoorgym='{0}' where room_no = '{1}'".format(
                            n, rno)
                        A = 'Outdoor Gym'
                        sr = sr+n*680
                        mycur8.execute(q)
                print(colorText(
                    "[[yellow-background]]---------->Your Extra Services Bill is:[[black-background]] "), sr)
                q = "Update Services_bill set Services_bill='{0}' where room_no='{1}'".format(
                    sr, rno)
                mycur8.execute(q)
                cn.commit()
                ex = input(
                    colorText("Press [[green]]ENTER[[white]] to return"))
                os.system('cls')
                print(colorText(a))
                print(colorText(b))
                ch = int(input("Enter the Choice: "))
            elif ch == 9:
                # revenue_generated
                mycur9 = cn.cursor()

                q = """select cust_data.room_no,cust_data.name,cust_data.Total_Room_Cost,
                    food_bill.food_bill,laundry_bill.laundry_bill,b.bar_bill,car.carrent_bill,g.game_bill,
                    s.services_bill,a.amusement_bill,
                    sum(Total_Room_cost+Food_bill+laundry_bill+bar_bill+carrent_bill+game_bill+
                    services_bill+amusement_bill) 'TOTAL COST'
                    from cust_data,food_bill,laundry_bill,amusement_bill as a,bar_bill as b,
                    carrent_bill as car,game_bill as g,services_bill as s
                    where cust_data.room_no=food_bill.room_no and cust_data.room_no=laundry_bill.room_no
                    and cust_data.room_no=b.room_no and cust_data.room_no=a.room_no and
                    cust_data.room_no=car.room_no and cust_data.room_no=g.room_no and
                    cust_data.room_no=s.room_no group by cust_data.room_no;"""
                mycur9.execute(q)
                data = mycur9.fetchall()

                print(colorText("[[red]]+"+("-"*192)+"+[[white]]"))

                print(colorText("[[red]]|[[blue]]R_No  \t[[red]]|[[blue]]Name    \t[[red]]|[[blue]]R_Cost \t[[red]]|[[blue]]Food     \t[[red]]|[[blue]]Laundry \t[[red]]|[[blue]]Bar     \t[[red]]|[[blue]]CarRent \t[[red]]|[[blue]]Game   \t[[red]]|[[blue]]Services \t[[red]]|[[blue]]Amusement \t[[red]]|[[blue]]Total Cost\t[[red]]|[[blue]]Discount\t[[red]]|[[blue]]TotAmt.[[red]]|[[white]]   "))
                print(colorText("[[red]]+"+("-"*192)+"+[[white]]"))

                for x in data:
                    print(colorText("[[red]]|[[white]]"), end="")
                    for y in range(0, len(x)):
                        if y == 0:
                            print(x[y], end='   \t')
                        elif y > len(x) - 2:
                            print(colorText('[[red]]|[[white]]'),
                                  x[y], end='     \t')
                            if x[y] >= 200000:
                                print(
                                    colorText('[[red]]|[[white]]'), "10%", end='     \t')
                                res = x[y]
                                res -= res * decimal.Decimal(0.1)
                            elif x[y] >= 160000:
                                print(
                                    colorText('[[red]]|[[white]]'), "20%", end='     \t')
                                res = x[y]
                                res -= res * decimal.Decimal(0.2)
                            elif x[y] >= 120000:
                                print(
                                    colorText('[[red]]|[[white]]'), "30%", end='     \t')
                                res = x[y]
                                res -= res * decimal.Decimal(0.3)
                            else:
                                print(
                                    colorText('[[red]]|[[white]]'), "0", end='     \t')
                                res = x[y]
                            print(colorText('[[red]]|[[white]]'), int(
                                res), end='     \t')
                        else:
                            print(colorText('[[red]]|[[white]]'),
                                  x[y], end='     \t')
                    print(colorText("[[red]]|[[white]]"))
                print(colorText("[[red]]+"+("-"*192)+"+[[white]]"))
                cn.commit()
                ex = input(
                    colorText("Press [[green]]ENTER[[white]] to return"))
                os.system('cls')
                print(colorText(a))
                print(colorText(b))
                ch = int(input("Enter the Choice: "))
            elif ch == 10:
                # Bill Generartion
                mycur10 = cn.cursor()
                rno = int(input("Enter the room number: "))
                q = """select cust_data.room_no,cust_data.name,cust_data.Total_Room_Cost,
                    food_bill.food_bill,laundry_bill.laundry_bill,b.bar_bill,car.carrent_bill,g.game_bill,
                    s.services_bill,a.amusement_bill,
                    sum(Total_Room_cost+Food_bill+laundry_bill+bar_bill+carrent_bill+game_bill+
                    services_bill+amusement_bill) 'TOTAL COST'
                    from cust_data,food_bill,laundry_bill,amusement_bill as a,bar_bill as b,
                    carrent_bill as car,game_bill as g,services_bill as s
                    where cust_data.room_no=food_bill.room_no and cust_data.room_no=laundry_bill.room_no
                    and cust_data.room_no=b.room_no and cust_data.room_no=a.room_no and
                    cust_data.room_no=car.room_no and cust_data.room_no=g.room_no and
                    cust_data.room_no=s.room_no and cust_data.room_no={0} group by cust_data.room_no;""".format(rno)
                mycur10.execute(q)
                data = mycur10.fetchall()

                print(colorText("[[red]]+"+("-"*192)+"+[[white]]"))

                print(colorText("[[red]]|[[blue]]R_No  \t[[red]]|[[blue]]Name    \t[[red]]|[[blue]]R_Cost \t[[red]]|[[blue]]Food     \t[[red]]|[[blue]]Laundry \t[[red]]|[[blue]]Bar     \t[[red]]|[[blue]]CarRent \t[[red]]|[[blue]]Game   \t[[red]]|[[blue]]Services \t[[red]]|[[blue]]Amusement \t[[red]]|[[blue]]Total Cost\t[[red]]|[[blue]]Discount\t[[red]]|[[blue]]TotAmt.[[red]]|[[white]]   "))
                print(colorText("[[red]]+"+("-"*192)+"+[[white]]"))
                for x in data:
                    print(colorText("[[red]]|[[white]]"), end="")
                    for y in range(0, len(x)):
                        if y == 0:
                            print(x[y], end='   \t')
                        elif y > len(x) - 2:
                            print(colorText('[[red]]|[[white]]'),
                                  x[y], end='     \t')
                            if x[y] >= 200000:
                                print(
                                    colorText('[[red]]|[[white]]'), "10%", end='     \t')
                                res = x[y]
                                res -= res * decimal.Decimal(0.1)
                            elif x[y] >= 160000:
                                print(
                                    colorText('[[red]]|[[white]]'), "20%", end='     \t')
                                res = x[y]
                                res -= res * decimal.Decimal(0.2)
                            elif x[y] >= 120000:
                                print(
                                    colorText('[[red]]|[[white]]'), "30%", end='     \t')
                                res = x[y]
                                res -= res * decimal.Decimal(0.3)
                            else:
                                print(
                                    colorText('[[red]]|[[white]]'), "0", end='     \t')
                                res = x[y]
                            print(colorText('[[red]]|[[white]]'), int(
                                res), end='     \t')
                        else:
                            print(colorText('[[red]]|[[white]]'),
                                  x[y], end='     \t')
                    print(colorText("[[red]]|[[white]]"))
                print(colorText("[[red]]+"+("-"*192)+"+[[white]]"))

                # paid
                mycur10.execute(
                    "DELETE FROM amusement_bill WHERE Room_no = {0}".format(rno))
                mycur10.execute(
                    "DELETE FROM bar_bill WHERE Room_no = {0}".format(rno))
                mycur10.execute(
                    "DELETE FROM carrent_bill WHERE Room_no = {0}".format(rno))
                mycur10.execute(
                    "DELETE FROM cust_data WHERE Room_no = {0}".format(rno))
                mycur10.execute(
                    "DELETE FROM food_bill WHERE Room_no = {0}".format(rno))
                mycur10.execute(
                    "DELETE FROM game_bill WHERE Room_no = {0}".format(rno))
                mycur10.execute(
                    "DELETE FROM laundry_bill WHERE Room_no = {0}".format(rno))
                mycur10.execute(
                    "DELETE FROM services_bill WHERE Room_no = {0}".format(rno))

                cn.commit()
                ex = input(
                    colorText("Press [[green]]ENTER[[white]] to return"))
                os.system('cls')
                print(colorText(a))
                print(colorText(b))
                ch = int(input("Enter the Choice: "))
        else:
            os.system('cls')
            print(colorText(a))
            print(colorText(
                """\t\t[[blue]]1][[white]] ADMIN\n\t\t[[red]]2][[white]] RECEPTION\n\t\t[[blue]]3][[white]] EXIT"""))
            ch1 = int(input("Enter the Choice: "))
    elif ch1 == 1:
        # For Admin
        os.system('cls')
        print(colorText(a))
        pwd = w.getpass()
        if pwd == "Sneh@1234":
            print(colorText("[[red]]Log in [[blue]]Successful[[white]]!!"))
            ex = input(colorText("Press [[green]]ENTER[[white]] to continue"))
            os.system('cls')
            print(colorText(a))
            print(colorText("[[red]]1.[[white]] View Statistics"))
            print(colorText("[[blue]]2.[[white]] Exit\n"))
            ch = int(input("Enter the Choice: "))
            os.system('cls')
            while ch != 2:
                import matplotlib.pyplot as p
                # Statistics
                x = -1
                while x != 3:
                    print(colorText(a))
                    print(colorText(
                        """[[red]]1.[[white]] Room-wise Profit\n[[blue]]2.[[white]] Field-wise Profit\n[[red]]3. [[white]]Exit\n"""))
                    x = int(input("Enter the Choice: "))
                    if x == 1:
                        mya1 = cn.cursor()
                        mya1.execute('delete from t1')
                        qq = """Insert into t1 select cust_data.room_no,cust_data.name,cust_data.Total_Room_Cost,
                            food_bill.food_bill,laundry_bill.laundry_bill,b.bar_bill,car.carrent_bill,g.game_bill,
                            s.services_bill,a.amusement_bill,
                            sum(Total_Room_cost+Food_bill+laundry_bill+bar_bill+carrent_bill+game_bill+
                            services_bill+amusement_bill) 'TOTAL COST'
                            from cust_data,food_bill,laundry_bill,amusement_bill as a,bar_bill as b,
                            carrent_bill as car,game_bill as g,services_bill as s
                            where cust_data.room_no=food_bill.room_no and cust_data.room_no=laundry_bill.room_no
                            and cust_data.room_no=b.room_no and cust_data.room_no=a.room_no and
                            cust_data.room_no=car.room_no and cust_data.room_no=g.room_no and
                            cust_data.room_no=s.room_no group by cust_data.room_no"""
                        mya1.execute(qq)

                        mya1.execute('select Room_No,Cost from t1')
                        data = mya1.fetchall()
                        R = []
                        C = []
                        for o in data:
                            for y in range(0, len(o)):
                                if o[0] not in R:
                                    R.append(o[0])
                                if o[1] not in C:
                                    C.append(o[1])
                        p.bar(R, C, color='brown')
                        p.xticks(R)
                        p.show()
                        ex = input(
                            colorText("Press [[green]]ENTER[[white]] to return"))
                        os.system('cls')
                    elif x == 2:
                        mya1 = cn.cursor()
                        q = """Insert into t1 select cust_data.room_no,cust_data.name,cust_data.Total_Room_Cost,
                            food_bill.food_bill,laundry_bill.laundry_bill,b.bar_bill,car.carrent_bill,g.game_bill,
                            s.services_bill,a.amusement_bill,
                            sum(Total_Room_cost+Food_bill+laundry_bill+bar_bill+carrent_bill+game_bill+
                            services_bill+amusement_bill) 'TOTAL COST'
                            from cust_data,food_bill,laundry_bill,amusement_bill as a,bar_bill as b,
                            carrent_bill as car,game_bill as g,services_bill as s
                            where cust_data.room_no=food_bill.room_no and cust_data.room_no=laundry_bill.room_no
                            and cust_data.room_no=b.room_no and cust_data.room_no=a.room_no and
                            cust_data.room_no=car.room_no and cust_data.room_no=g.room_no and
                            cust_data.room_no=s.room_no group by cust_data.room_no"""
                        mya1.execute(q)
                        mya1.execute('''select sum(Food_bill),sum(laundry_bill),sum(bar_bill),
                                        sum(carrent_bill),sum(game_bill),sum(Services_bill),
                                        sum(amusement_bill) from t1 ''')
                        data = mya1.fetchall()
                        l = []
                        for o in data:
                            for y in range(0, len(o)):
                                l.append(o[y])
                        l1 = [0, 1, 2, 3, 4, 5, 6]
                        p.plot(l1, l, 'r.', linestyle='--')
                        c = ['Restro', 'Laundry', 'Bar', 'CarRent',
                             'Game', 'Services', 'Amusement']
                        p.xticks(l1, c)
                        p.show()
                        ex = input(
                            colorText("Press [[green]]ENTER[[white]] to return"))
                        os.system('cls')
                else:
                    os.system('cls')
                    print(colorText(a))
                    print(colorText("[[red]]1.[[white]] View Statistics"))
                    print(colorText("[[blue]]2.[[white]] Exit\n"))
                    ch = int(input("Enter the Choice: "))
                    os.system('cls')
            os.system('cls')
            print(colorText(a))
            print(colorText(
                """\t\t[[blue]]1][[white]] ADMIN\n\t\t[[red]]2][[white]] RECEPTION\n\t\t[[blue]]3][[white]] EXIT"""))
            ch1 = int(input("Enter the Choice: "))
            os.system("cls")
        else:
            os.system("cls")
            print(
                colorText("[[red]]Incorrect [[blue]]Password[[white]]!!\n\tENTER Again"))


def end(t):
    os.system('cls')
    col, row = os.get_terminal_size()
    row = row-1

    t1 = ' thank you '
    t2 = 'logging off'
    dot = '.'*int((col-10-len(t)-len(t1)-len(t2))/4)
    s = '|#'+dot + t1 + dot+'#| '+t+' |#'+dot + t2 + dot+'#|'
    l = len(s)

    a1 = r"     _____     "
    a2 = r"  __/__|__\__  "
    a3 = r" /  _ +++ _  \ "
    a4 = r"'--(_)---(_)--'"

    w1 = r"  ___  ___   ___  ___    _____   _____ "
    w2 = r" / __|/ _ \ / _ \|   \  | _ ) \ / / __|"
    w3 = r"| (_ | (_) | (_) | |) | | _ \\ V /| _| "
    w4 = r" \___|\___/ \___/|___/  |___/ |_| |___|"

    sp = ' '*(int((l-len(a4)-len(w3))/2)-2)
    w1 = sp+w1+sp
    w2 = sp+w2+sp
    w3 = sp+w3+sp
    w4 = sp+w4+sp
    ws = ' '*len(w3)

    n = int((row-9)/2)-1
    for y in range(l, -1, -1):
        os.system('cls')
        for x in range(n):
            print(s[:y])
        print("")
        print('')
        print(ws[0:y]+a1+w1[y:])
        print(ws[0:y]+a2+w2[y:])
        print(ws[0:y]+a3+w3[y:])
        print(ws[0:y]+a4+w4[y:])
        print("="*l)
        print("")
        print('')
        for x in range(n):
            print(s[:y])
        time.sleep(0.00000000001)
    input('')
    os.system('cls')
    return


end('Grandeur Resort')
