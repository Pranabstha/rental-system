def display_welcome_message():
    print("*************************************************************************************************")
    print("                                  welcome To Bike Maagement System                               ")
    print("*************************************************************************************************")
    print("\n")
    # displays the welcome msg 

def display_main_menu():
    print("please select the given option below")
    print("1. Sell bikes")
    print("2. Order bikes")
    print("3. Exit")
    # displays the main main menu 

def display_sell_bikes():
    print("\n")
    print("Let's sell bikes")
    print("\n")
    #enter the sell bikes option


def display_order_bikes():
    print("\n")
    print("Let's order bikes")
    print("\n")
    #enter the Order bikes option

def display_exit():
    print("*************************************************************************************************")
    print("                              Thank you for interacting with us, Do visit us soon                ")
    print("*************************************************************************************************")
    #displayes the exit programme

def display_invalid_input():
    print("\n")
    print("Invalid input. Please enter one of the number provided")
    print("\n")
    #displayes invalid input error



def return_2d_list():
    list_2d = []
    file = open("bikes.txt")
    for line in file:
        line = line.replace("\n","")
        line = line.split(",")
        list_2d.append(line)#append the value of line in to lis_2D
    file.close()
    return(list_2d)
    #return the bikes.txt files in 2D list



def show_bikes():
    print("__________________________________________________________________________________________________\n")
    print("Bike ID\t\tBike-Name\t\tCompany\t\tColor\t\tStock\t\tPrice")
    print("__________________________________________________________________________________________________\n")
    #file = open("bikes.txt","r")
    bike_id = 1

    for bike in bikes_2D:
        #print(" ",bike_id,"\t\t"+line.replace(",","\t"))
        print("|" + " "*4 + str(bike_id) + " "* 4 + "|" + bike[0] + " "*(22-len(bike[0])) + "|" + bike[1] + " "*(19-len(bike[1])) + "|" + bike[2] + " "*(19-len(bike[2])) + "|" + bike[3] + " "*(11-len(bike[3])) + "|" + bike[4] + " "*(13-len(bike[4])) )
        bike_id += 1
    print("__________________________________________________________________________________________________\n")
    #file.close()
    #reads/ diplays the bikes.txt file


def valid_bikes_id():
    input_validity = False
    while input_validity == False:
        try:
            validBikesId = int(input("Enter ID of the bikes : "))
        except:
            display_invalid_input()
        else:
            input_validity = True
    while validBikesId <=0 or validBikesId >= len(return_2d_list()):
        print("please provide a valid bike ID!!!!")
        show_bikes()
        validBikesId = int(input("Enter ID of the bikes : "))
    return validBikesId
        #takes the bike ID from the user and and checks the it is valid or not


def order_valid_stock(bike_id):
    bikes = return_2d_list()
    quant = int(bikes[bike_id - 1][3])#since bike_Id starts from index 1 changing into index 0
    if(int(quant) > 0 ):
        quantity = int(input("Enter the quantity of the bike"))
        while quantity > int(quant):
            print("provide valid quantity number")
            quantity = int(input("Enter the quantity of the bike"))
        return quantity
            

def sell_valid_stock(bike_id):
    bikes = return_2d_list()
    quant = int(bikes[bike_id - 1][3])#since bike_Id starts from index 1 changing into index 0
    if(quant) > 0 or (quant) <=(bikes[bike_id - 1][3]):
        return quant #cheching the stocks are avaliable or not

'''def sell_valid_stock(bike_id):
    list_2d = return_2d_list()
    print(len(list_2d))
    if int(list_2d[bike_id -1][])'''


def update_stock_order(bike_id,quantity):
    order_show = return_2d_list()
    order_show[bike_id - 1][3] = str(int(order_show[bike_id - 1][3]) + quantity)
    return order_show
    #updating the stocks in bikes.txt file after ordering bikes 



def get_info():
    import datetime
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    mins = str(datetime.datetime.now().minute)
    random = year + month + day + hour + mins
    return random
    # impoting date adn time (year/month/date and hour:minutes)

def order_input():
    order_Name = input("enter dis name : ")
    order_address = input("enter the address : ") 
    order_number = input("enter the number : ")
    order_bikes = return_2d_list()
    ordered_bikes =[]
    total_price = 0
    ordercount = True 
    order_bikeID = valid_bikes_id()
    while ordercount == True:
        valid = False
        while valid == False:
            try:
                order_quantity = int(input("enter the quantity you want to order : "))
            except:
                print("No of Quantity not avaliable currently")
            else:
                valid = True
        if order_quantity > 0 :
            item = order_bikes[order_bikeID-1]
            item[3] = order_quantity
            order_update = update_stock_order(order_bikeID,order_quantity)
            order_price = int(order_bikes[ order_bikeID -1][4].replace("$",""))
            order_update_file(order_update)
            order_indiviual_price = int(order_price * order_quantity)
            total_price = total_price + order_indiviual_price
            ordered_bikes.append(item)
            continue_order = input("do u want to continue (y/n)").lower()
            if continue_order == "n":
                ordercount = False
                order_bill(order_Name,order_address,order_number, ordered_bikes,total_price)
                print_order_bill(order_Name,order_address,order_number,ordered_bikes, total_price)
                display_main_menu()
            else:
                show_bikes()
        else:
            print("quantity must me greater tha 0 ")

        #taking input for ordering and printing the order bill

def order_update_file(list):
    file = open("bikes.txt","w")
    for bikes in list:
        file.write(str(bikes[0])+","+str(bikes[1])+","+str(bikes[2])+","+str(bikes[3])+","+str(bikes[4])+"\n")
    file.close
    #updating the bike.txt file after ordering bikes


def order_bill(name,address,phone,order_bikes, tot_price):#printing order bill
    import datetime
    file= open(name + get_info()+".txt","w")
    file.write(" ___________________________________________________________________________________________________________\n")
    file.write("                                           Order Bill                                                        \n")
    file.write("____________________________________________________________________________________________________________\n")
    file.write("\n")
    file.write("Name : " + name +"\n")
    file.write("Address : " + address +"\n")
    file.write("Phone : "+ str(phone) +"\n")
    file.write("Date : " + str(datetime.datetime.now().year)+"/"+ str(datetime.datetime.now().month)+"/"+str(datetime.datetime.now().day)+"\t"+"Time : " + str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+"\n")  
    file.write("_________________________________________________________________________________________________\n")
    file.write("Bike Name \t\t company \t\t color \t\t stocks \t\t Price per unit \n")
    file.write("_________________________________________________________________________________________________\n")

    for rides in order_bikes:
        for i in range(len(rides)):
            file.write(str(rides[i]))
            file.write(str("\t\t"))
        file.write("\n")
    file.write("_________________________________________________________________________________________________\n")
    file.write("Total Price : " + str(tot_price)+"\n")
    file.write(" ___________________________________________________________________________________________________________\n")
    file.write("                         Thank you for Ordering the bike ,Do visit Again                                     \n")
    file.write("____________________________________________________________________________________________________________\n")
    file.close
    #creating the bill after ordering the bikes

def print_order_bill(name,address,phone,order_bikes, tot_price):
    import datetime
    print(" ___________________________________________________________________________________________________________")
    print("                                           Order Bill                                                        ")
    print("____________________________________________________________________________________________________________")
    print("\n")
    print("Name : " + name +"\n")
    print("Address : " + address +"\n")
    print("Phone : "+ str(phone) +"\n")
    print("Date : " + str(datetime.datetime.now().year)+"/"+ str(datetime.datetime.now().month)+"/"+str(datetime.datetime.now().day)+"\t"+"Time : " + str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+"\n")  
    print("_________________________________________________________________________________________________")
    print("Bike Name \t\t company \t\t color \t\t stocks \t\t Price per unit  ")
    print("_________________________________________________________________________________________________")

    for rides in order_bikes:
        for i in range(len(rides)):
            print(str(rides[i]),end="")
            print(str("\t\t"),end="")
        print("\n")
    print("_________________________________________________________________________________________________")
    print("Total Price : " + str(tot_price)+"\n")
    print(" ___________________________________________________________________________________________________________")
    print("                         Thank you for Ordering the bike ,Do visit Again                                    ")
    print("____________________________________________________________________________________________________________")
    #printing bill for Ordering bill

            


def sell_input():
    sell_Name = input("enter your name : ")
    sell_address = input("enter your address : ") 
    sell_number = input("enter your phone number : ")
    sell_bikes = return_2d_list()
    selled_bikes =[]
    total_price = 0
    sell_count= True 
    while sell_count == True:
        sell_bikeID = valid_bikes_id()
        valid = False
        while valid == False:
            try:
                sell_quantity = int(input("enter the quantity you want to Sell : "))
            except:
                print("Please enter quantity correctly")
            else:
                valid = True
        if sell_quantity > 0 and sell_quantity < sell_valid_stock(sell_bikeID):
            sell_valid_stock(sell_bikeID)
            item = sell_bikes[sell_bikeID-1]
            item[3] = sell_quantity
            sell_update = update_stock_sell(sell_bikeID,sell_quantity)
            sell_price = int((sell_bikes[sell_bikeID -1][4]).replace("$",""))
            sell_update_file(sell_update)
            sell_indiviual_price = str(int(sell_price * sell_quantity))
            total_price = total_price + int(sell_indiviual_price)
            selled_bikes.append(item)
            continue_sell = input("do u want to continue (y/n)").lower()
            if continue_sell == "n":
                sell_count = False
                sell_bill(sell_Name,sell_address,sell_number,selled_bikes,total_price)
                print_sell_bill(sell_Name,sell_address,sell_number,selled_bikes, total_price)
                display_main_menu()
            else:
                show_bikes()
        else:
            print("please enter a valid Quantity")

            #taking input for ordering and printing the order bill

def sell_bill(sell_Name,sell_address,sell_phone,order_bikes, tot_price):#printing order bill
    import datetime
    file= open(sell_Name + get_info()+".txt","w")
    file.write(" ___________________________________________________________________________________________________________\n")
    file.write("                                           Sell Bill                                                        \n")
    file.write("____________________________________________________________________________________________________________\n")
    file.write("\n")
    file.write("Name : " + sell_Name +"\n")
    file.write("Address : " + sell_address +"\n")
    file.write("Phone : " + str(sell_phone) +"\n")
    file.write("Date : " + str(datetime.datetime.now().year)+"/"+ str(datetime.datetime.now().month)+"/"+str(datetime.datetime.now().day)+"\t"+"Time : " + str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+"\n")  
    file.write("_________________________________________________________________________________________________\n")
    file.write("Bike Name \t\t company \t\t color \t\t stocks \t\t Price per unit \n")
    file.write("_________________________________________________________________________________________________\n")

    for rides in order_bikes:
        for i in range(len(rides)):
            file.write(str(rides[i]))
            file.write(str("\t\t"))
        file.write("\n")
    file.write("_________________________________________________________________________________________________\n")
    file.write("Total Price : " + "$"+str(tot_price)+"\n")
    file.write(" ___________________________________________________________________________________________________________\n")
    file.write("                         Thank you for Selling the bike ,Do visit Again                                     \n")
    file.write("____________________________________________________________________________________________________________\n")
    file.close
    #creating the sell after Selling the bikes

def print_sell_bill(name,address,phone,order_bikes, tot_price):
    import datetime
    print(" ___________________________________________________________________________________________________________")
    print("                                           sell Bill                                                        ")
    print("____________________________________________________________________________________________________________")
    print("\n")
    print("Name : " + name +"\n")
    print("Address : " + address +"\n")
    print("Phone : "+ str(phone) +"\n")
    print("Date : " + str(datetime.datetime.now().year)+"/"+ str(datetime.datetime.now().month)+"/"+str(datetime.datetime.now().day)+"\t"+"Time : " + str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+"\n")
    print("_________________________________________________________________________________________________")
    print("Bike Name \t\t company \t\t color \t\t stocks \t\t Price per unit")
    print("_________________________________________________________________________________________________")

    for rides in order_bikes:
        for i in range(len(rides)):
            print(str(rides[i]),end="")
            print(str("\t\t"),end="")
        print("\n")
    print("_________________________________________________________________________________________________")
    print("Total Price : " + "$"+str(tot_price)+"\n")
    print(" ___________________________________________________________________________________________________________")
    print("                         Thank you for Selling the bike ,Do visit Again                                    ")
    print("____________________________________________________________________________________________________________")

    #printing bill for sell bill

def sell_update_file(list):
    file = open("bikes.txt","w")
    for bikes in list:
        file.write(str(bikes[0])+","+str(bikes[1])+","+str(bikes[2])+","+str(bikes[3])+","+str(bikes[4])+"\n")
    file.close
#updating file after selling bikes

def update_stock_sell(bike_id,quantity):
    sell_show = return_2d_list()
    sell_show[bike_id - 1][3] = str(int(sell_show[bike_id - 1][3]) - quantity)
    return sell_show
#updating the stocks in bikes.txt file after selling bikes 




