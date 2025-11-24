print("="*50)
print("AIRPORT MANAGEMENT SYSTEM")
print("="*50)
print("INIT Mandatory Authentication Procedure...")

from tabulate import tabulate

def mainmenu():
    print("\nWelcome to the Airport Manager Dashboard.")
    print("="*50)
    print("INFORMATION INTERFACE")
    print("="*50)
    print("1. Airline Information","\n2. Flight Information","\n3. Passangers Information ","\n4. Employee Information","\n5. Exit Software") # Added Exit option to the printed menu
    
    info_index = 0
    
    while True:
        try:
            print("="*50)
            info_index = int(input("Enter index of required information:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        if info_index == 1:
            Airline_Information()
        elif info_index == 2:
            Flight_Information()
        elif info_index == 3:
            Passenger_Information()
        elif info_index == 4:
            Employee_Information()
        elif info_index == 5:
            print("EXITING SOFTWARE...")
            quit()
        else:
            print("Invalid index. Please select from 1 to 5.")

def validationyesno(inputyesno):
    while True:
        userinputyesno = input(inputyesno).lower().strip()
        if userinputyesno in ["yes", "no", "y", "n"]:
            return "yes" if userinputyesno.startswith("y") else "no"
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def Airline_Information():
    airline_data = []
    airline_data_headers = ["Airline Name", "Airline Aircraft", "No. of Destinations"]

    airline_data_choice = "yes"
    
    while airline_data_choice == "yes":
        
        print("="*50)
        print("WELCOME TO AIRLINE INFORMATION")
        print("="*50)
        print("1. Add airline data")
        print("2. Remove airline data")
        print("3. Display")
        
        airline_menu_choice = -1
        while airline_menu_choice not in [1, 2, 3]:
            try:
                airline_menu_choice = int(input("Enter airline data choice (1, 2, or 3):"))
            except ValueError:
                print("Invalid input. Please enter a number (1, 2, or 3).")
                continue
            
            if airline_menu_choice not in [1, 2, 3]:
                print("Invalid input. Please enter a number (1, 2, or 3).")


        if airline_menu_choice == 1:
            airline_data_add_choice = "yes"
            while airline_data_add_choice == "yes":
                print("\nAdding Airline Data")
                airline_name = input("Enter name of operating Airline:").strip()
                airline_aircraft = input("Enter quantity of Aircraft at the Airport:").strip()
                airline_dest_no = input(f"How many destinations is {airline_name} flying to:").strip()
                airline_data_data = [airline_name, airline_aircraft, airline_dest_no]
                airline_data.append(airline_data_data)
                print("Data updated!")
                
                airline_data_add_choice = validationyesno("Do you wish to continue adding data? (yes/no):")
            
            airline_data_choice = validationyesno("Do you wish to continue with airline info? (yes/no):")
            
            # Removed redundant mainmenu() call here
            
        elif airline_menu_choice == 2:
            if not airline_data:
                print("The airline data list is empty. Nothing to remove.")
            else:
                airline_data_delete_choice = "yes"
                while airline_data_delete_choice == "yes":
                    airline_name_del = input("\nEnter name of airline to remove:").lower().strip()
                    
                    found_and_deleted = False
                    
                    for entry in airline_data[:]: 
                        if airline_name_del == entry[0].lower(): 
                            airline_data.remove(entry)
                            found_and_deleted = True
                            print(f"Successfully removed data for {entry[0]}.")
                            break
                    
                    if not found_and_deleted:
                        print(f"Airline '{airline_name_del}' not found in the list.")
                        
                    print("\n--- Current Data ---")
                    if airline_data:
                        print(tabulate(airline_data, headers=airline_data_headers, tablefmt="fancy_grid"))
                    else:
                        print("The list is now empty.")

                    airline_data_delete_choice = validationyesno("Do you wish to continue deleting data? (yes/no):")

            airline_data_choice = validationyesno("Do you wish to continue with this module? (yes/no):")
            
            # Removed redundant mainmenu() call here

        elif airline_menu_choice == 3:
            if airline_data:
                airline_data_table = tabulate(airline_data, headers=airline_data_headers, tablefmt="fancy_grid")
                print("\nCurrent Airline Data")
                print(airline_data_table)
            else:
                print("The airline data list is empty.")
            
            airline_data_choice = validationyesno("Do you wish to continue with this module? (yes/no):")
            
            # Removed redundant mainmenu() call here

def Flight_Information():
    flight_information_data = []
    flight_information_data_headers = ["AIRLINE", "FLT NO.", "GATE", "DEPARTURE", "ETA", "STATUS", "RUNWAY", "APPROACH/DEP"]
    flight_info_data_choice = "yes"

    while flight_info_data_choice == "yes":
        print("="*50)
        print("WELCOME TO FLIGHT INFORMATION")
        print("="*50)
        print("1. Add flight data")
        print("2. Remove flight data")
        print("3. Display")
        
        flight_menu_choice = -1
        while flight_menu_choice not in [1, 2, 3]:
            try:
                flight_menu_choice = int(input("Enter flight data choice (1, 2, or 3):"))
            except ValueError:
                print("Invalid input. Please enter a number (1, 2, or 3).")
                continue
            
            if flight_menu_choice not in [1, 2, 3]:
                 print("Invalid input. Please enter a number (1, 2, or 3).")

        if flight_menu_choice == 1:
            flight_data_add_choice = "yes"
            while flight_data_add_choice == "yes":
                print("\nAdding Flight Data")
                
                airline_op = input("Enter Operating Airline:").strip()
                flight_no = input("Enter Flight Number (e.g., AA123):").strip() 
                gate_assigned = input("Enter Gate Assigned:").strip()
                time_dep = input("Enter Time of Departure (HH:MM):").strip()
                eta = input("Enter Estimated Time of Arrival (ETA):").strip()
                status = input("Enter Status Type (Takeoff/Landing,on time/delay):").strip()
                runway = input("Enter Runway Assigned:").strip()
                approach_dep = input("Enter Approach/Departure info Type :").strip()
                
                flight_data_entry = [airline_op, flight_no,gate_assigned, time_dep, eta, status,runway, approach_dep]
                flight_information_data.append(flight_data_entry)
                print("Data updated!")
                flight_data_add_choice = validationyesno("Do you wish to continue adding data? (yes/no):")
            
            flight_info_data_choice=validationyesno("Do you wish to continue with flight data info? (yes/no):")
            
            # Removed redundant mainmenu() call here
            
        elif flight_menu_choice == 2:
            if not flight_information_data:
                print(" The flight data list is empty. Nothing to remove.")
            else:
                flight_data_delete_choice = "yes"
                while flight_data_delete_choice == "yes":
                    flight_id_del = input("\nEnter Flight Number to remove:").lower().strip()
                    
                    found_and_deleted = False
                    
                    for entry in flight_information_data[:]: 
                        if flight_id_del == entry[1].lower(): 
                            flight_information_data.remove(entry)
                            found_and_deleted = True
                            print(f" Successfully removed Flight {entry[1]} ({entry[0]}).")
                            break
                    if not found_and_deleted:
                        print(f" Flight '{flight_id_del.upper()}' not found in the list.")
                    print("\n--- Current Data ---")
                    if flight_information_data:
                        print(tabulate(flight_information_data, headers=flight_information_data_headers, tablefmt="fancy_grid"))
                    else:
                        print("The list is now empty.")

                    flight_data_delete_choice=validationyesno("Do you wish to continue deleting data? (yes/no):")
                
                flight_info_data_choice=validationyesno("Do you wish to continue with flight data info? (yes/no):")
                
                # Removed redundant mainmenu() call here
                
        elif flight_menu_choice == 3:
            if flight_information_data:
                flight_data_table = tabulate(flight_information_data, headers=flight_information_data_headers, tablefmt="fancy_grid")
                print("\n Current Flight Data")
                print(flight_data_table)
            else:
                print("The flight data list is empty.")
                
            flight_info_data_choice=validationyesno("Do you wish to continue with flight data info? (yes/no):")
            
            # Removed redundant mainmenu() call here

def Passenger_Information():
    passenger_data = []
    passenger_data_headers = ["Passenger Name", "PNR", "Flight No."]
    passenger_data_choice = "yes"
    
    while passenger_data_choice == "yes":
        print("="*50)
        print("WELCOME TO PASSENGER INFORMATION")
        print("="*50)
        print("1. Add passenger data")
        print("2. Remove passenger data")
        print("3. Display")
        
        pax_menu_choice = -1
        while pax_menu_choice not in [1, 2, 3]:
            try:
                pax_menu_choice = int(input("Enter pax data choice (1, 2, or 3):"))
            except ValueError:
                print("Invalid input. Please enter a number (1, 2, or 3).")
                continue
            
            if pax_menu_choice not in [1, 2, 3]:
                 print("Invalid input. Please enter a number (1, 2, or 3).")

        if pax_menu_choice == 1:
            passenger_data_add_choice = "yes"
            while passenger_data_add_choice == "yes":
                print("\nAdding Passenger Data")
                pax_name = input("Enter Passenger Name:").strip()
                pnr = input("Enter PNR (Passenger Name Record):").strip()
                flight_no = input("Enter Flight Number (e.g., AA123):").strip()
                
                passenger_data_entry = [pax_name, pnr, flight_no]
                passenger_data.append(passenger_data_entry)
                print("Data updated!")
                
                passenger_data_add_choice = validationyesno("Do you wish to continue adding data? (yes/no):")
            
            passenger_data_choice = validationyesno("Do you wish to continue with passanger info? (yes/no):")
            
            # Removed redundant mainmenu() call here
            
        elif pax_menu_choice == 2:
            if not passenger_data:
                print("The passenger data list is empty. Nothing to remove.")
            else:
                passenger_data_delete_choice = "yes"
                while passenger_data_delete_choice == "yes":
                    pnr_del = input("\nEnter PNR to remove:").lower().strip()
                    
                    found_and_deleted = False
                    
                    for entry in passenger_data[:]: 
                        if pnr_del == entry[1].lower(): 
                            passenger_data.remove(entry)
                            found_and_deleted = True
                            print(f" Successfully removed PNR {entry[1]} ({entry[0]}).")
                            break
                    
                    if not found_and_deleted:
                        print(f"PNR '{pnr_del.upper()}' not found in the list.")
                        
                    print("\n--- Current Data ---")
                    if passenger_data:
                        print(tabulate(passenger_data, headers=passenger_data_headers, tablefmt="fancy_grid"))
                    else:
                        print("The list is now empty.")
                    passenger_data_delete_choice = validationyesno("Do you wish to continue deleting data? (yes/no):")
                
                passenger_data_choice = validationyesno("Do you wish to continue with passanger info? (yes/no):")
                
                # Removed redundant mainmenu() call here

        elif pax_menu_choice == 3:
            if passenger_data:
                passenger_data_table = tabulate(passenger_data, headers=passenger_data_headers, tablefmt="fancy_grid")
                print("\nCurrent Passenger Data")
                print(passenger_data_table)
            else:
                print("The passenger data list is empty.")
                
            passenger_data_choice = validationyesno("Do you wish to continue with this module? (yes/no):")
            
            # Removed redundant mainmenu() call here

def Employee_Information():
    employee_data = []
    employee_data_headers = ["Employee ID", "Employee Name", "Job Title", "Salary", "Shift"]
    employee_data_choice = "yes"
    
    while employee_data_choice == "yes":
        print("="*50)
        print("WELCOME TO EMPLOYEE INFORMATION")
        print("="*50)
        print("1. Add employee data")
        print("2. Remove employee data")
        print("3. Display all data")
        print("4. Reports (Average/Min/Max Salary)")
        print("5. Exit Module")
        
        emp_menu_choice = -1
        while emp_menu_choice not in [1, 2, 3, 4, 5]:
            try:
                emp_menu_choice = int(input("Enter employee data choice (1, 2, 3, 4, 5):"))
            except ValueError:
                print("Invalid input. Please enter a number (1, 2, 3, 4, 5).")
                continue
            
            if emp_menu_choice not in [1, 2, 3, 4, 5]:
                 print("Invalid input. Please enter a number (1, 2, 3, 4, 5).")

        if emp_menu_choice == 1:
            employee_data_add_choice = "yes"
            while employee_data_add_choice == "yes":
                print("\n Adding Employee Data")
                
                emp_id = input("Enter Employee ID:").strip()
                emp_name = input("Enter Employee Name:").strip()
                emp_job = input("Enter Employee Job Title:").strip()
                
                while True:
                    emp_salary_str = input("Enter Employee Salary:").strip()
                    try:
                        emp_salary = float(emp_salary_str)
                        break
                    except ValueError:
                        print("Invalid input. Salary must be a number.")

                emp_shift = input("Enter Employee Shift (e.g., Day/Night):").strip()
                
                employee_data_entry = [emp_id, emp_name, emp_job, emp_salary, emp_shift]
                employee_data.append(employee_data_entry)
                print("Data updated!")
                
                employee_data_add_choice = validationyesno("Do you wish to continue adding data? (yes/no):")
            
            employee_data_choice = validationyesno("Do you wish to continue with employee info? (yes/no):")
            
        elif emp_menu_choice == 2:
            if not employee_data:
                print("The employee data list is empty. Nothing to remove.")
            else:
                employee_data_delete_choice = "yes"
                while employee_data_delete_choice == "yes":
                    emp_id_del = input("\nEnter Employee ID to remove:").lower().strip()
                    found_and_deleted = False
                    
                    for entry in employee_data[:]: 
                        if emp_id_del == entry[0].lower(): 
                            employee_data.remove(entry)
                            found_and_deleted = True
                            print(f"Successfully removed Employee ID {entry[0]} ({entry[1]}).")
                            break
                    
                    if not found_and_deleted:
                        print(f"Employee ID '{emp_id_del.upper()}' not found in the list.")
                        
                    print("\n--- Current Data ---")
                    if employee_data:
                        print(tabulate(employee_data, headers=employee_data_headers, tablefmt="fancy_grid"))
                    else:
                        print("The list is now empty.")

                    employee_data_delete_choice = validationyesno("Do you wish to continue deleting data? (yes/no):")

            employee_data_choice = validationyesno("Do you wish to continue with this employee info? (yes/no):")

        elif emp_menu_choice == 3:
            if employee_data:
                employee_data_table = tabulate(employee_data, headers=employee_data_headers, tablefmt="fancy_grid")
                print("\nCurrent Employee Data")
                print(employee_data_table)
            else:
                print("The employee data list is empty.")
            
            employee_data_choice = validationyesno("Do you wish to continue with this employee info? (yes/no):")
            
        elif emp_menu_choice == 4:
            print("\nSalary Reports")
            if not employee_data:
                print("Cannot generate reports: Employee data list is empty.")
            else:
                salaries = [entry[3] for entry in employee_data]
                total_salary = sum(salaries)
                count = len(salaries)
                average_salary = total_salary / count
                print(f"Total Employees: {count}")
                print(f"Average Salary: ${average_salary:,.2f}")

                max_salary = max(salaries)
                max_earners = [entry[1] for entry in employee_data if entry[3] == max_salary]
                max_earners_str = ", ".join(max_earners)
                print(f"Highest Salary: ${max_salary:,.2f} (Earners: {max_earners_str})")
                
                min_salary = min(salaries)
                min_earners = [entry[1] for entry in employee_data if entry[3] == min_salary]
                min_earners_str = ", ".join(min_earners)
                print(f"Lowest Salary: ${min_salary:,.2f} (Earners: {min_earners_str})")
            
            employee_data_choice = validationyesno("Do you wish to continue with this employee info? (yes/no):")
            
            # Removed redundant mainmenu() call here
            
        elif emp_menu_choice == 5:
            print("Exiting Employee Information Module.")
            employee_data_choice = "no"
            
            # Return from the function to go back to the mainmenu loop

# --- Login Logic ---
login_attempts = 0
max_attempts = 3
authenticated = False

while login_attempts < max_attempts:
    login = input("Enter username: ")
    password = input("Enter password: ")
    print("PROCESSING REQUEST...")
    
    if login == "admin" and password == "airport_admin_123":
        print("Successful Login!")
        authenticated = True
        break
    else:
        login_attempts += 1 
        
        if login_attempts < max_attempts:
            print(f"Invalid Credentials. You have {max_attempts - login_attempts} tries remaining.")
        else:
            print("BREACH DETECTED. SYSTEM LOCKED.") # Added final lock message

if authenticated:
    print("Authenticated...")
    mainmenu()
# No need for the final else block, as the login loop handles the failure message.