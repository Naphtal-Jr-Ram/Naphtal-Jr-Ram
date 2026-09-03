import os
from datetime import datetime

# Declaration of text files
CREDENTIALS_FILE = "users.txt"
HISTORY_FILE = "history.txt"
UNPAID_FILE = "unpaid.txt"
MALL1_FILE = "mall1.txt"
MALL2_FILE = "mall2.txt"
MALL3_FILE = "mall3.txt"
name = ""

def get_last_entry_time(name):
    with open(HISTORY_FILE, "r") as f:
        lines = f.readlines()
    for line in reversed(lines):  # Search backwards
        user, action, time = line.strip().split(",")
        if user == name and action == "ENTRY":
            return time
    return None

#Gateway Menu Function
def Gate_Menu(name):
    print("\n\nCustomer Menu:\n1. Vehicle entry\n2. Vehicle exit\n3. View History\n4. Pay Outstanding fees\n5. Logout ")
    choice4 = int(input("Enter your choice (1,2,3,4): "))
    match choice4:
        case 1:
            # Vehicle entry
            entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(MALL1_FILE, "a") as f1, open(HISTORY_FILE, "a") as f2:
                f1.write(f"{name},ENTRY,{entry_time}\n")
                f2.write(f"{name},ENTRY,{entry_time}\n")
            print(f"Vehicle entry for {name} recorded at {entry_time}")
            Gate_Menu(name)  # Return to Gateway(First Mall) Menu.
        case 2:
            # Vehicle time exit
            exit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(MALL1_FILE, "a") as f1, open(HISTORY_FILE, "a") as f2:
                f1.write(f"{name},EXIT,{exit_time}\n")
                f2.write(f"{name},EXIT,{exit_time}\n")
            print(f"Vehicle exit for {name} recorded at {exit_time}")

            # Calculations for payment
            price = 15
            print(f"Balance to pay R{price}")
            choice5 = input(f"Do you want to pay fee of {price}?(yes/no)").lower()
            if choice5 == "yes":
                # Payment and storage
                with open(MALL1_FILE, "a") as f1, open(HISTORY_FILE, "a") as f2:
                    f1.write(f"{name} payed {price}\n")
                    f2.write(f"{name} payed {price}\n")
                print(f"The amount R{price} has been debited from your account for {name}")
            elif choice5 == "no":
                # Store to outstanding fees
                price = 15
                with open(UNPAID_FILE, "a") as f1, open(MALL1_FILE, "a") as f2:
                    f1.write(f"{name}, UNPAID {price}\n")
                    f2.write(f"{name}, UNPAID {price}\n")
            else:
                print("Invalid option\n")
            Gate_Menu(name)  # Return to gateway(First Mall) menu
        case 3:
            print(f"\nHistory for {name}:")
            with open(HISTORY_FILE, "r") as f:
                for line in f:
                    user, action, time = line.strip().split(",")
                    if user == name:
                        print(f"{name}, {action} at {time}")
            print("\n History of UNPAID payments:") #History of Unpaid payments.
            with open(UNPAID_FILE, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0].strip() == name:  # Check if first value of line is equal to string stored in name
                        print(line.strip()) #Print all lines associated with user
                    else:
                        print("No Unpaid History yet!!")
            Gate_Menu(name)  # Return to gateway(First Mall) menu

        case 4:
            # outstanding fees
            # Open the file and read line by line
            price = 0 #Initially set price_out to zero
            with open(UNPAID_FILE, "r") as f:
                for line in f:
                    # Strip whitespace and split by comma
                    parts = line.strip().split(",")
                    if parts[0].strip() == name: #Check if first value of line is equal to string stored in name
                        print(line.strip()) #print all lines associated with user with name
                        price += price #Sum all values stored in unpaid file.
                        print(f"Amount you owe is R{price}")
                        outfees = input("Pay all Outstanding fees?(yes/no): ")
                        if outfees == "yes":
                            # Read all lines from the file
                            with open(UNPAID_FILE, "r") as f:
                                lines = f.readlines()

                                # Filter out lines where the first column matches 'user'
                                filtered_lines = []
                                for line in lines:
                                    parts = line.strip().split(",")
                                    if parts[0].strip() != user:
                                        filtered_lines.append(line)

                                    # Write back only the filtered lines
                                    with open("data.txt", "w") as f:
                                        f.writelines(filtered_lines)
                                print(f"All Outstanding fees associated with {name} have been paid.")
                    else:
                        print("No Unpaid History yet!!")

            Gate_Menu(name)  # Return to gateway(First Mall) menu
        case 5:
            main(name)

def Pavil_Menu(name):
    print("\n\nCustomer Menu:\n1. Vehicle entry\n2. Vehicle exit\n3. View History\n4. Pay Outstanding fees\n5. Logout ")
    choice4 = int(input("Enter your choice (1,2,3,4): "))
    match choice4:
        case 1:
            # Vehicle entry
            entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(HISTORY_FILE, "a") as f1, open(MALL2_FILE, "a") as f2:
                f1.write(f"{name},ENTRY,{entry_time}\n")
                f2.write(f"{name},EXIT,{entry_time}\n")
            print(f"Vehicle entry for {name} recorded at {entry_time}")
            Pavil_Menu(name)  # Return to Pavillion mall menu
        case 2:
            # Vehicle time exit
            exit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(HISTORY_FILE, "a") as f1, open(MALL2_FILE, "a") as f2:
                f1.write(f"{name},EXIT,{exit_time}\n")
                f2.write(f"{name},EXIT,{exit_time}\n")
            print(f"Vehicle exit for {name} recorded at {exit_time}")

            # Calculations for payment
            entry_time = get_last_entry_time(name)
            if entry_time:
                fmt = "%Y-%m-%d %H:%M:%S"
                hr = (datetime.strptime(exit_time, fmt) - datetime.strptime(entry_time, fmt)).seconds / 3600
                print(f"Parking duration: {hr:.2f} hours")

            price = 10 + 10 * hr
            choice5 = input(f"Do you want to pay fee of {price}?(yes/no)").lower()
            if choice5 == "yes":
                # Payment and storage

                with open(HISTORY_FILE, "a") as f1, open(MALL2_FILE, "a") as f2:
                    f1.write(f"{name} payed {price}\n")
                    f2.write(f"{name} payed {price}\n")
                print(f"The amount R{price} has been debited from your account for {name}")
            elif choice5 == "no":
                # Store to outstanding fees
                with open(UNPAID_FILE, "a") as f1, open(MALL2_FILE, "a") as f2:
                    f1.write(f"{name}, UNPAID {price}\n")
                    f2.write(f"{name}, UNPAID {price}\n")
            else:
                print("Invalid option\n")
                Pavil_Menu()  # Return to Pavillion mall menu
            Pavil_Menu(name)  # Return to Pavillion mall menu
        case 3:
            print(f"\nHistory for {name}:")
            # Accessing History file
            with open(HISTORY_FILE, "r") as f:
                for line in f:
                    user= line.strip().split(",")
                    if user == name:
                        print(f"{name}, {action} at {time}")
            print("\n History of UNPAID payments:")
            with open(UNPAID_FILE, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0].strip() == name:  # Check if first value of line is equal to string stored in name
                        print(line.strip())
            Pavil_Menu(name)  # Return to Pavillion mall menu
        case 4:
            # outstanding fees
            # Open the file and read line by line
            price = 0  # Initially set price_out to zero
            with open("unpaid.txt", "r") as f:
                for line in f:
                    # Strip whitespace and split by comma
                    parts = line.strip().split(",")
                    if parts[0].strip() == name:  # Check if first value of line is equal to string stored in name
                        print(line.strip())  # print all lines associated with user with name
                        price += price  # Sum all values stored in unpaid file associated with user.
            print(f"Amount you owe is R{price}")
            outfees = input("Pay all Outstanding fees?(yes/no): ")
            if outfees == "yes":
                # Read all lines from the file
                with open("unpaid.txt", "r") as f:
                    lines = f.readlines()

                    # Filter out lines where the first column matches 'user'
                    filtered_lines = []
                    for line in lines:
                        parts = line.strip().split(",")
                        if parts[0].strip() != user:
                            filtered_lines.append(line)

                # Write back only the filtered lines
                with open("data.txt", "w") as f:
                    f.writelines(filtered_lines)

                print(f"All Outstanding fees associated with {name} have been paid.")
            Pavil_Menu(name)  # Return to Pavillion mall menu
        case 5:  # Logout option returns user to main menu
            main(name)

def LaLucia_menu(name):
    print("\n\nCustomer Menu:\n1. Vehicle entry\n2. Vehicle exit\n3. View History\n4. Pay Outstanding fees\n5. Logout ")
    choice4 = int(input("Enter your choice (1,2,3,4): "))
    match choice4:
        case 1:
            # Vehicle entry registration
            entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(HISTORY_FILE, "a") as f1, open(MALL3_FILE, "a") as f2:
                f1.write(f"{name},ENTRY,{entry_time}\n")
                f2.write(f"{name},ENTRY,{entry_time}\n")
            print(f"Vehicle entry for {name} recorded at {entry_time}")
            LaLucia_menu(name)  # Return to LaLucia's main menu
        case 2:
            # Vehicle time exit storage
            exit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(HISTORY_FILE, "a") as f1, open(MALL3_FILE, "a") as f2:
                f1.write(f"{name},EXIT,{exit_time}\n")
                f2.write(f"{name},EXIT,{exit_time}\n")
            print(f"Vehicle exit for {name} recorded at {exit_time}")

            # Calculations for payment
            entry_time = get_last_entry_time(name)
            if entry_time:
                fmt = "%Y-%m-%d %H:%M:%S"
                hr = (datetime.strptime(exit_time, fmt) - datetime.strptime(entry_time, fmt)).seconds / 3600
                print(f"Parking duration: {hr:.2f} hours")


            if hr <= 5:
                price = 12 + (12 * hr)
            else:
                price = 60
            choice5 = input(f"Do you want to pay fee of {price}?(yes/no)").lower()
            if choice5 == "yes":
                # Payment and storage
                with open(HISTORY_FILE, "a") as f1, open(MALL3_FILE, "a") as f2:
                    f1.write(f"{name} payed {price}\n")
                    f2.write(f"{name} payed {price}\n")
                print(f"The amount R{price} has been debited from your account {name}")
            elif choice5 == "no":
                # Store to outstanding fees
                with open(UNPAID_FILE, "a") as f1, open(MALL3_FILE, "a") as f2:
                    f1.write(f"{name}, UNPAID {price}\n")
                    f2.write(f"{name}, UNPAID {price}\n")
            else:
                print("Invalid option\n")
                LaLucia_Menu(name)  # Return to LaLucia's main menu
            LaLucia_menu(name)  # Return to LaLucia's main menu
        case 3:
            print(f"\nHistory for {name}:")
            # Access History file
            with open(HISTORY_FILE, "r") as f:
                for line in f:
                    user= line.split(",")
                    if user == name:
                        print(f"{name}, {action} at {time}")
            print("\n History of UNPAID payments:")
            with open(UNPAID_FILE, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0].strip() == name:  # Check if first value of line is equal to string stored in name
                        print(line.strip())
            LaLucia_menu(name)  # Return to LaLucia's main menu
        case 4:
            # outstanding fees
            # Open the file and read line by line
            price = 0  # Initially set price_out to zero
            with open("unpaid.txt", "r") as f:
                for line in f:
                    # Strip whitespace and split by comma
                    parts = line.strip().split(",")
                    if parts[0].strip() == name:  # Check if first value of line is equal to string stored in name
                        print(line.strip())  # print all lines associated with user with name
                        price += price  # Sum all values stored in unpaid file associated with user.
            print(f"Amount you owe is R{price}")
            outfees = input("Pay all Outstanding fees?(yes/no): ")
            if outfees == "yes":
                # Read all lines from the file
                with open("unpaid.txt", "r") as f:
                    lines = f.readlines()

                # Filter out lines where the first column matches 'user'
                    filtered_lines = []
                    for line in lines:
                        parts = line.strip().split(",")
                        if parts[0].strip() != user:
                            filtered_lines.append(line)

                # Write back only the filtered lines
                with open("data.txt", "w") as f:
                    f.writelines(filtered_lines)

                print(f"All Outstanding fees associated with {name} have been paid.")
            else:
                print("Returning to main menu.\n")
                main(name)
            LaLucia_Menu(name)  # Return to LaLucia's main menu
        case 5:
            main(name)

#Definition of Parking Admin Menu
def PA_menu(name):
    print("Select mall")
    print("1. Gateway(flat Rate R15, Capacity 250\n2. Pavillion(R10/hr, capacity 180\n3. LaLucia( R12/hr capped @R60, Capacity 150")
    option = int(input("Enter your choice: "))
    if option == 1:
        print("\n=================Daily Activity: MALL1:================== ")
        with open("mall1.txt", "r") as f:
            lines = f.readlines() #Read all lines
        # Print each line
            for line in lines:
                print(line.strip())
        print("----------------------------------------------------------")
        PA_menu(name)
    elif option == 2:
        print("\n================Daily Activity: MALL2:=========================== ")
        with open("mall2.txt", "r") as f:
            # Read all lines
            lines = f.readlines()

            # Print each line
            for line in lines:
                print(line.strip())
        print("------------------------------------------------------------")
        PA_menu(name)

    elif option == 3:
        print("\n=======================Daily Activity: MALL3:========================= ")
        with open("mall3.txt", "r") as f:
            # Read all lines
            lines = f.readlines()

            # Print each line
            for line in lines:
                print(line.strip())
        print("-----------------------------------------------------------------------------")
        PA_menu()
    else:
        print("INVALID OPTION!!")
        PA_menu(name)



#Defining entire main code as function named main
def main(name):
    #Display list of actions
    print("1. Register\n2. Login\n3. Exit")
    choice1 = int(input("Enter your choice: "))
    match choice1: #Evaluating integer stored at choice1
        case 1:  #If integer is of value 1(Registration)
            print("\nYou chose to register....\nWhich user are you:")
            print("1. Customer\n2. Admin\n3. Owner\n!!!Type role using lower case!!!")  #Display list of roles
            choice2 = input("Enter your choice: ").lower()
            match choice2:  #Evaluating string choice 2
                case "customer":    #If string entered is customer
                    #Ask user for name and password
                    name = input("Enter your name: ")
                    password = input("Enter your password: ")

                    #Store credentials in credentials file
                    with open(CREDENTIALS_FILE, "a") as f:
                        f.write(f"{name},{password}\n")
                    print("Registration successful!\n")

                    #Call main function
                    main(name)
                case "admin":   #if string is admin
                    #Ask username and password
                    name = input("Enter your name: ")
                    password = input("Enter your password: ")

                    #store username and password into credentials file
                    with open(CREDENTIALS_FILE, "a") as f:
                        f.write(f"{name},{password}\n")
                    print("Registration successful!\n")

                    #Call function main by name
                    main(name)

                case "owner":   #if string is owner
                    #Ask for username and password
                    name = input("Enter your name: ")
                    password = input("Enter your password: ")

                    #Store credentials entered prior
                    with open(CREDENTIALS_FILE, "a") as f:
                        f.write(f"{name},{password}\n")
                    print("Registration successful!\n")

                    #Call function by name
                    main(name)

                case _: #If string value is not part of the list
                    print("Invalid option") #Display invalid option

                    #Call main function
                    main(name)
        case 2: #Case 2 for Login
            print("You chose to login....\nWhich user are you:")
            print("1. Customer\n2. Parking Administrator\n3. Owner/Shareholder") #LIst of roles
            choice3 = int(input("Enter your choice: "))
            match choice3: #Evaluate variable match3 in below cases.
                case 1: #Value entered in match 3 is 1
                    #Ask for username and password
                    name = input("Enter your name: ")
                    password = input("Enter your password: ")

                    #Retrieval and if username exists
                    with open(CREDENTIALS_FILE, "r") as f:
                        for line in f:
                            stored_user, stored_pass = line.strip().split(",")
                            if stored_user == name and stored_pass == password:
                                print("Login successful! Welcome,", name)

                                #Display mall options
                                print("Select mall")
                                print("1. Gateway(flat Rate R15, Capacity 250\n2. Pavillion(R10/hr, capacity 180\n3. LaLucia( R12/hr capped @R60, Capacity 150")
                                choice3 = int(input("Enter your choice: "))
                                match choice3:
                                    case 1: # Gateway Mall/ First Mall Menu
                                        print("You chose Gateway mall...")
                                        Gate_Menu(name) #Call GateWay Function
                                    case 2:  # Pavillion/ Second Mall Menu
                                        print("You chose Pavillion mall...")
                                        Pavil_Menu(name) #Call Pavillion function
                                    case 3:  # LaLucia/ Third Mall Menu
                                        print("You chose LaLucia mall...")
                                        #Mall option
                                        LaLucia_menu(name)
                            else:
                                print("Username/password does not exist!!!\n")
                                main(name)
                case 2: #Parking administrator option
                    name = input("Enter your name: ")
                    password = input("Enter your password: ")
                    #Retrieval and if username exists
                    with open(CREDENTIALS_FILE, "r") as f:
                        for line in f:
                            stored_user, stored_pass = line.strip().split(",")
                            if stored_user == name and stored_pass == password:
                                print("Login successful! Welcome,", name)
                                PA_menu(name) #Call PA_Menu Function
                            else:
                                print("Username/password does not exist!!!\n")
                                main()

                case 3: #Owner option
                    name = input("Enter your name: ")
                    password = input("Enter your password: ")
                    #retrieval snd if username exists
                    with open(CREDENTIALS_FILE, "r") as f:
                        for line in f:
                            stored_user, stored_pass = line.strip().split(",")
                            if stored_user == name and stored_pass == password:
                                print("Login successful! Welcome,", name)
                                #Print all Data. ALL NECESSARY FILES.
                                print("\nDaily Activity: MALL1: ")
                                with open("mall1.txt", "r") as f:
                                    # Read all lines
                                    lines = f.readlines()

                                    # Print each line
                                    for line in lines:
                                        print(line.strip())

                                print("\nDaily Activity: MALL2: ")
                                with open("mall2.txt", "r") as f:
                                    # Read all lines
                                    lines = f.readlines()

                                    # Print each line
                                    for line in lines:
                                        print(line.strip())

                                print("\nDaily Activity: MALL3: ")
                                with open("mall3.txt", "r") as f:
                                    # Read all lines
                                    lines = f.readlines()

                                    # Print each line
                                    for line in lines:
                                        print(line.strip())
                                main(name)

                case _:#Invalid role
                    print("Invalid role")
                    main(name)
main(name)