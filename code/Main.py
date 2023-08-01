import function

continueLoop = True
function.display_welcome_message()
function.display_main_menu()
while continueLoop == True:
    continuationCode = input("Please enter the Given option above: ")
    if continuationCode == "1":
        function.display_sell_bikes()
        # Lists the bikes in the file
        function.show_bikes()
        function.sell_input()
        
    elif continuationCode == "2":
        function.display_order_bikes()
        function.show_bikes()
        function.order_input()

    elif continuationCode == "3":
        function.display_exit()
        continueLoop = False
    else:
        function.display_invalid_input()
        function.display_main_menu()



